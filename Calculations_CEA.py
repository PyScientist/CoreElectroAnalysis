import math
import numpy as np
from Prepare_data_CEA import prepare_two_row_data

class Statistics:
    """Statistics class provide methods for work with stat"""

    '''
    The standard deviation is the square
    root of the average of the squared deviations
    from the mean, i.e., std = sqrt(mean(abs(x - x.mean()) ** 2)).
    '''

    def __init__(self, selection):
        self.selection = np.array(selection)
        self.sum = None
        self.count = None
        self.max_val = None
        self.min_val = None
        self.mean = None
        self.std = None
        self.sigma = None
        self.three_sigma = None
        self.interval = None
        self.z_list = None

        self.create_stat_data()
        self.print_in_console()

    def create_stat_data(self):
        self.sum = np.sum(self.selection)
        self.count = len(self.selection)
        self.max_val = np.max(self.selection)
        self.min_val = np.min(self.selection)
        self.interval = self.max_val - self.min_val
        self.mean = np.mean(self.selection)
        self.std = np.std(self.selection)
        self.sigma = self.std**(1/2)
        self.three_sigma = self.sigma*3

    def print_in_console(self):
        print(F'Сумма элементов = {self.sum};')
        print(F'Колличество элементов = {self.count};')
        print(F'Максимальное значение = {self.max_val};')
        print(F'Минимальное значение = {self.min_val};')
        print(F'Интервал = {self.interval};')
        print(F'Среднее арифметическое значение = {self.mean};')
        print(F'Среднее квадратичное отклонение = {self.std};')
        print(F'Сигма = {self.sigma};')
        print(F'3 Сигма = {self.three_sigma};')



def calc_m(por, ff):
    m = None
    if por != None and ff != None:
       m = round(math.log(1/ff, por), 3)  # Porosity in v/v
    return m

def prepare_m_list(table):
    # Calculating m values and preparing a list with values for the entire sample selection
    m_list = []
    data_calc = prepare_two_row_data('POR', 'FF', table)
    for x in range(len(data_calc[0])):
        m_list.append(calc_m(data_calc[0][x], data_calc[1][x]))
    return m_list

def calculate_m(parent, row_to_exclude=[]):
    """
    Calculate среднее значение коэффициента m в уравнение Арчи по данным импортируемым из Таблицы
    входной параметр parent это ссылка на экземпляр класса основного приложения
    """
    data_calc = prepare_two_row_data('POR', 'FF', parent.InitDataTable)

    # Before using data remove all filtered rows
    for x in range(len(row_to_exclude)):
        data_calc[0].pop(row_to_exclude[x])
        data_calc[1].pop(row_to_exclude[x])

    m_list = []
    for x in range(len(data_calc[0])):
        m_list.append(calc_m(data_calc[0][x], data_calc[1][x]))  # porosity in v/v
    m_avg = np.mean(m_list)
    return m_avg

def prepare_m_hist_details(table, row_to_exclude=[]):
    # Расет значений m и подготовка списка с значениями по всей выборке
    m_list = []
    # Подготовка данных для расчета (импорт из таблицы)
    data_calc = prepare_two_row_data('POR', 'FF', table)

    # Before using data remove all filtered rows
    for x in range(len(row_to_exclude)):
        data_calc[0].pop(row_to_exclude[x])
        data_calc[1].pop(row_to_exclude[x])

    for x in range(len(data_calc[0])):
        m_list.append(calc_m(data_calc[0][x], data_calc[1][x]))
    count, bins = np.histogram(m_list)
    return count, bins