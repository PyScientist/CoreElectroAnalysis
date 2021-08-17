import sys, os

from PyQt5.QtGui import QIcon,\
                        QPixmap

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QApplication,\
                            QMainWindow,\
                            QFileDialog, \
                            QVBoxLayout

from CoreElectroAnalysisMainWindow import Ui_MainWindow

from matplotlib import pyplot as plt

from Prepare_data_CEA import prepare_table_data_from_txt, \
                             put_table_in_qtable_wiget, \
                             modify_cells, \
                             mnemonics_adjustments, \
                             set_uniq_data_to_listwidget, \
                             find_checked_categiries, \
                             row_filter_for_categories, \
                             prepare_one_row_data

from Mpl_CEA import MyMplCanavas,\
                    prepare_abstract_canvas_and_toolbar,\
                    prepare_canvas, plot_m_mean_line,\
                    plot_data_on_por_ff,\
                    plot_hist_of_m,\
                    plot_data_on_por_m

from Calculations_CEA import calculate_m, Statistics

from ToolButtonsOperate import ButtonsSetForPorosityMAnalysis

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class of mainwindow of application with method of launching of data processing and visualisation
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()

    def widgets_adjust(self):
        """
        Method for additional adjustment of widgets in main window of the application
        """
        self.setWindowTitle('CoreElectroAnalysis v2.2 -- copyright Dmitriev S.A. 01.11.2020 --')
        self.setWindowIcon(QIcon(QPixmap('./figures/application_icon_core_sample.png')))

        # Button for choose name of the source file for analysis
        self.InitFilePathSetButton.clicked.connect(self.choose_init_data_file_dialog)
        self.InitFilePathSetButton.setIcon(QIcon(QPixmap('./figures/find_files_for_upload.png')))
        self.InitFilePathSetButton.setIconSize(QSize(30, 30))

        # Button for uploading data to the application (widget QTableWidget)
        self.LoadDataButton.clicked.connect(self.load_data)
        self.LoadDataButton.setIcon(QIcon(QPixmap('./figures/Load_Data.png')))
        self.LoadDataButton.setIconSize(QSize(50, 50))

        # Button for category choosing
        self.GetCategoriesButton.clicked.connect(self.initialize_categories)

        # Button for report on studied data preporation
        self.PlotReportButton.toggled.connect(self.plot_report)
        # Button for plotting porosity-ff and mean value m function to matpotlib widget
        self.PlotGraphButton.clicked.connect(self.plot_data)
        # Button for displaying the chart Matplotlib Porosity-m and tools to this diagram
        self.AdjustPorosityMButton.clicked.connect(self.adjust_porosity_m_method)
        # Creating a vertical placement in the QWidget widget for displaying graphs


        self.companovka_for_mpl = QVBoxLayout(self.MplWidget)
        # Creating a vertical placement in the QWidget widget to display the toolbar for porosity-m
        self.ToolPaletteVerticalLayout = QVBoxLayout(self.ToolbarWidget)

    def adjust_porosity_m_method(self):

        # Check of what we have in the QWidget dedicated to plot graphs and delete all widgets from this place
        self.del_members(self.companovka_for_mpl.parent().children()[1:])

        # Create canvas and toolbar for m-porosity comparison
        canvas, toolbar = prepare_abstract_canvas_and_toolbar(layout=self.companovka_for_mpl)

        # Get link to axes and plot the data
        axes = canvas.figure.get_children()[1]
        axes.cla()
        plot_data_on_por_m(table=self.InitDataTable, axes=axes, row_to_exclude=self.rows_not_satisfy_filter)

        # Check is the tools-palette for porosity-m exist if it is delete it
        if hasattr(self, 'ButtonsSetForPorosityMAnalysis'):
            self.ButtonsSetForPorosityMAnalysis.delete_buttons_set()
            del self.ButtonsSetForPorosityMAnalysis

        # Create Tools palette
        self.ButtonsSetForPorosityMAnalysis = ButtonsSetForPorosityMAnalysis(self.ToolPaletteVerticalLayout, self)

    def plot_report(self):

        # find out what categories are chosen for further processing
        checked_dict = find_checked_categiries(self.listWidget_well_chose,self.listWidget_zone_chose, self.listWidget_lith_chose)
        # find out the row numbers rows which not satisfying the selection criteria
        self.rows_not_satisfy_filter = row_filter_for_categories(checked_dict, self.InitDataTable)

        data_for_stat = prepare_one_row_data('POR', self.InitDataTable)
        # Before using data remove all filtered rows
        for x in range(len(self.rows_not_satisfy_filter)):
            data_for_stat[0].pop(self.rows_not_satisfy_filter)

        stat = Statistics(data_for_stat)


    def choose_init_data_file_dialog(self):
        """
        Method for selecting the file path by searching the standard file selection dialog
        """
        fname = QFileDialog.getOpenFileName(self, 'Choose data file for Core Electro Analysis (txt file)', './data/')
        print(self.InitFilePathField.fontPointSize())
        self.InitFilePathField.setText(fname[0])
        font = self.InitFilePathField.font()
        font.setPointSize(12)
        self.InitFilePathField.setFont(font)

    def load_data(self):
        """
        Method for importing data from a file and placing it in a table widget
        """
        file_path = self.InitFilePathField.toPlainText()
        if os.path.isfile(file_path):
            data_voc = prepare_table_data_from_txt(file_path)

            mnemonics_adjustments(data_voc['header'])

            put_table_in_qtable_wiget(data_voc['header'], self.InitDataTable, data_voc['data'])
            modify_cells(self.InitDataTable)
        else:
            print (F"File {file_path} is not exists, please correct path and try one more time!")

        set_uniq_data_to_listwidget(self.InitDataTable, self.listWidget_well_chose, "WELL")
        set_uniq_data_to_listwidget(self.InitDataTable, self.listWidget_zone_chose, "ZONE")
        set_uniq_data_to_listwidget(self.InitDataTable, self.listWidget_lith_chose, "LITH")


    def initialize_categories(self):
        pass

    def plot_data(self):
        """Method for performing calculations and plotting data in matplotlib figures"""

        # find out what categories are chosen for further processing
        checked_dict = find_checked_categiries(self.listWidget_well_chose,self.listWidget_zone_chose, self.listWidget_lith_chose)
        # find out the row numbers rows which not satisfying the selection criteria
        self.rows_not_satisfy_filter = row_filter_for_categories(checked_dict, self.InitDataTable)


        self.del_members(self.companovka_for_mpl.parent().children()[1:])

        # Check is the tool-palette for porosity-m exist if it is delete it
        if hasattr(self, 'ButtonsSetForPorosityMAnalysis'):
            self.ButtonsSetForPorosityMAnalysis.delete_buttons_set()
            del self.ButtonsSetForPorosityMAnalysis

        # Adding a widget with a matplotlib canvas to display the scatter chart
        canvas, toolbar = prepare_abstract_canvas_and_toolbar(layout=self.companovka_for_mpl)

        # Adding a widget with a matplotlib canvas to display the histogram
        canvas1 = prepare_canvas(layout=self.companovka_for_mpl)

        # Getting a link to axis 1
        axes = canvas.figure.get_children()[1]

        # Calling methods for displaying a function and placing source data on a scatter chart
        axes.cla()

        axes.grid(True, c='lightgrey', alpha=0.5, which='major')
        axes.grid(True, c='lightgrey', alpha=0.2, which='minor')

        # Getting a link to axis 2
        axes1 = canvas1.figure.get_children()[1]

        # Call method of displaying histogram of m values
        axes1.cla()
        axes1.grid(True, c='lightgrey', alpha=0.5, which='major')

        if self.combobox_mode.currentText() == 'general':

            # Calculating the average value of m for the selected source data
            m_avg = calculate_m(self, row_to_exclude=self.rows_not_satisfy_filter)

            plot_m_mean_line(m_avg=m_avg, axes=axes)
            plot_data_on_por_ff(table=self.InitDataTable, axes=axes, row_to_exclude=self.rows_not_satisfy_filter)
            # Print avg value of m for a=1 on cross-plot
            axes.annotate(F'The average value of "m"={round(m_avg, 3)}', xy=(0.015, 3))
            axes.annotate(F'The "a" value = 1', xy=(0.015, 1.5))

            plot_hist_of_m(table=self.InitDataTable, axes=axes1, row_to_exclude=self.rows_not_satisfy_filter)

        elif self.combobox_mode.currentText() == 'sampling':
            pass
        else:
            pass

    @staticmethod
    def del_members(widgets):
        """Function for delete widget in main field of matplotlib widgets placements"""
        for widget in widgets:
            widget.setParent(None)
            if isinstance(widget, MyMplCanavas):
                plt.close(widget.figure)
            del widget


def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
   main_application()