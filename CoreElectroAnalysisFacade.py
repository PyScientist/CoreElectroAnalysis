import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QFileDialog, QToolButton, QVBoxLayout
from CoreElectroAnalysisMainWindow import Ui_MainWindow

from Prepare_data_CEA import prepare_table_data_from_txt, put_table_in_qtable_wiget, modify_cells
from Mpl_CEA import prepare_canvas_and_toolbar, prepare_canvas, plot_m_mean_line, plot_data_on_por_ff, plot_hist_of_m, plot_data_on_por_m
from Calculations_CEA import calculate_m


class ButtonsSetPorosityMAnalysis:
    '''
    Tools for andjustment Porosity-M plot
    '''
    def __init__(self, parent):
        self.Button_plot_porosity_m_function = QToolButton()
        self.Button_plot_porosity_m_function.setText('m=f(Por)')
        self.Button_plot_porosity_m_function.setObjectName('Button_plot_porosity_m_function')
        parent.VerticalLayuot4.addWidget(self.Button_plot_porosity_m_function)

    def delete_buttons_set(self):
        self.Button_plot_porosity_m_function.setParent(None)
        del self.Button_plot_porosity_m_function

class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Класс основного окна приложения с методами для запуска обработки данных
    '''

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.widgets_adjust()

    def widgets_adjust(self):
        '''
        Метод для донастройки виджетов в главном окне программы
        '''

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
        self.AdjustPorosityMButton.clicked.connect(self.adjustPorosityMMethod)

        # Создание вертикального размещения в виджете QWidget
        self.companovka_for_mpl = QVBoxLayout(self.MplWidget)
        # Добавляем виджет с холстом матплотлиб для отображеня диаграммы рассеяния
        self.canvas, self.toolbar = prepare_canvas_and_toolbar(layout=self.companovka_for_mpl)
        # Добавляем виджет с холстом матплотлиб для отображеня гистограммы
        self.canvas1 = prepare_canvas(layout=self.companovka_for_mpl)

    def adjustPorosityMMethod(self):
        if hasattr(self, 'canvas'):
            self.canvas.setParent(None)
            del self.canvas
        if hasattr(self, 'canvas1'):
            self.canvas1.setParent(None)
            del self.canvas1
        if hasattr(self, 'toolbar'):
            self.toolbar.setParent(None)
            del self.toolbar

        self.canvas, self.toolbar = prepare_canvas_and_toolbar(layout=self.companovka_for_mpl)

        # Получение ссылки на оси 1
        axes = self.canvas.figure.get_children()[1]
        axes.cla()
        plot_data_on_por_m(table=self.InitDataTable, axes=axes)

        if hasattr(self, 'VerticalLayout4'):
            pass
        else:
            self.VerticalLayuot4 = QVBoxLayout()
            self.ToolbarWidget.setLayout(self.VerticalLayuot4)
            self.ButtonsSetPorosityMAnalysis = ButtonsSetPorosityMAnalysis(self)

        print('The print finished')

    def show_hide_hist_widget(self, state):
        if hasattr(self, 'canvas1'):
            if state == True:
               self.canvas1.setVisible(False)
            if state == False:
               self.canvas1.setVisible(True)
        else:
            'This canvas (hist of m values) is absent'
            self.ButtonsSetPorosityMAnalysis.delete_buttons_set()
            del self.ButtonsSetPorosityMAnalysis

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
        '''
        Метод для расчета и отображения данных
        '''
        if hasattr(self, 'canvas1') & hasattr(self, 'canvas'):
           # Рассчитываем среднее значение m для выбранных исходных данных
           m_avg = calculate_m(self)

           # Получение ссылки на оси 1
           axes = self.canvas.figure.get_children()[1]

           # Вызов методов отображения функции и помещения на диаграмму рассеяния исходных данных
           axes.cla()
           plot_m_mean_line(m_avg = m_avg, axes = axes)
           plot_data_on_por_ff(table=self.InitDataTable, axes=axes)

           # Получение ссылки на оси 2
           axes1 = self.canvas1.figure.get_children()[1]
           # Вызываем метод отображения гистограммы значений m
           axes1.cla()
           plot_hist_of_m(table=self.InitDataTable, axes=axes1)
        else:
            'These canvas (hist of m values or porosity-FF) are absent'


def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main_application()