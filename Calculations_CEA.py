import math
import numpy as np
from Prepare_data_CEA import prepare_two_row_data


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
    Расчитываем среднее значение коэффициента m в уравнение Арчи по данным импортируемым из Таблицы
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