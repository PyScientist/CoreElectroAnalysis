import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QFileDialog, QToolButton, QVBoxLayout
from CoreElectroAnalysisMainWindow import Ui_MainWindow

from matplotlib import pyplot as plt

from Prepare_data_CEA import prepare_table_data_from_txt, put_table_in_qtable_wiget, modify_cells
from Mpl_CEA import MyMplCanavas, prepare_abstract_canvas_and_toolbar, prepare_canvas, plot_m_mean_line, plot_data_on_por_ff, plot_hist_of_m, plot_data_on_por_m
from Calculations_CEA import calculate_m

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

        self.setWindowTitle('CoreElectroAnalysis')

        # Кнопка установки имни исходного фала
        self.InitFilePathSetButton.clicked.connect(self.choose_init_data_file_dialog)
        # Кнопка для загрузки данных в программу (виджет QTableWudget)
        self.LoadDataButton.clicked.connect(self.import_data)
        # Кнопка для включения и отклюения гистограммы значений m
        self.Mpl_hide_show_button.toggled.connect(self.show_hide_hist_widget)
        # Кнопка для обработки и отображения данных в виджетах matpotlib
        self.PlotGraphButton.clicked.connect(self.plot_data)
        # Кнопка для отображения диаграммы Matplotlib Пористость-m и инструментов к этой диаграмме
        self.AdjustPorosityMButton.clicked.connect(self.adjust_porosity_m_method)
        # Создание вертикального размещения в виджете QWidget для отображения графиков
        self.companovka_for_mpl = QVBoxLayout(self.MplWidget)
        # Создание вертикального размещения в виджете QWidget для отображения панели инструментов
        self.ToolPaletteVerticalLayout = QVBoxLayout(self.ToolbarWidget)

    def adjust_porosity_m_method(self):

        def del_members(widgets):
            for widget in widgets:
                widget.setParent(None)
                if isinstance(widget, MyMplCanavas):
                    plt.close(widget.figure)
                del widget

        # Check of what we have in the QWidget dedicated to plot graphs and delete all widgets from this place
        del_members(self.companovka_for_mpl.parent().children()[1:])

        # Create canvas and toolbar for m-porosity comparison
        canvas, toolbar = prepare_abstract_canvas_and_toolbar(layout=self.companovka_for_mpl)

        # Get link to axes and plot the data
        axes = canvas.figure.get_children()[1]
        axes.cla()
        plot_data_on_por_m(table=self.InitDataTable, axes=axes)

        # Check is the tools-palette for porosity-m exist if it is delete it
        if hasattr(self, 'ButtonsSetForPorosityMAnalysis'):
            self.ButtonsSetForPorosityMAnalysis.delete_buttons_set()
            del self.ButtonsSetForPorosityMAnalysis

        # Create Tools palette
        self.ButtonsSetForPorosityMAnalysis = ButtonsSetForPorosityMAnalysis(self.ToolPaletteVerticalLayout, self)

    def show_hide_hist_widget(self, state):
        pass

    def choose_init_data_file_dialog(self):
        '''
        Метод для выбора пути к файлу путем выхова стандартного диалога выбора файла
        '''
        fname = QFileDialog.getOpenFileName(self, 'Choose data file for electro-analysis', './data/')
        self.InitFilePathField.setText(fname[0])

    def import_data(self):
        '''
        Метод для импорта данных из файла и помещения их в виджет таблицы
        '''
        file_path = self.InitFilePathField.toPlainText()
        data_voc = prepare_table_data_from_txt(file_path)
        put_table_in_qtable_wiget(data_voc['header'], self.InitDataTable, data_voc['data'])
        modify_cells(self.InitDataTable)

    def plot_data(self):
        """Метод для расчета и отображения данных"""

        def del_members(widgets):
            for widget in widgets:
                widget.setParent(None)
                if isinstance(widget, MyMplCanavas):
                    plt.close(widget.figure)
                del widget

        del_members(self.companovka_for_mpl.parent().children()[1:])

        # Check is the tool-palette for porosity-m exist if it is delete it
        if hasattr(self, 'ButtonsSetForPorosityMAnalysis'):
            self.ButtonsSetForPorosityMAnalysis.delete_buttons_set()
            del self.ButtonsSetForPorosityMAnalysis

        # Добавляем виджет с холстом матплотлиб для отображеня диаграммы рассеяния
        canvas, toolbar = prepare_abstract_canvas_and_toolbar(layout=self.companovka_for_mpl)

        # Добавляем виджет с холстом матплотлиб для отображеня гистограммы
        canvas1 = prepare_canvas(layout=self.companovka_for_mpl)

        # Рассчитываем среднее значение m для выбранных исходных данных
        m_avg = calculate_m(self)

        # Получение ссылки на оси 1
        axes = canvas.figure.get_children()[1]

        # Вызов методов отображения функции и помещения на диаграмму рассеяния исходных данных
        axes.cla()
        plot_m_mean_line(m_avg = m_avg, axes = axes)
        plot_data_on_por_ff(table=self.InitDataTable, axes=axes)

        # Получение ссылки на оси 2
        axes1 = canvas1.figure.get_children()[1]
        # Вызываем метод отображения гистограммы значений m
        axes1.cla()
        plot_hist_of_m(table=self.InitDataTable, axes=axes1)

def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main_application()