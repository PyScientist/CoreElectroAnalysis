import math
import numpy as np
from Prepare_data_CEA import prepare_two_row_data

def calculate_m(parent):
    '''
    Расчитываем среднее значение коэффициента m в уравнение Арчи по данным импортируемым из Таблицы
    входной параметр parent это ссылка на экземпляр класса основного приложения
    '''
    # Подготовка данных для расчета (импорт из таблицы)
    data_calc = prepare_two_row_data('POR', 'FF', parent.InitDataTable)
    # Расет значений m и подготовка списка с значениями по всей выборке
    m_list = []
    for x in range(len(data_calc[0])):
        m_list.append(math.log(1 / data_calc[1][x], data_calc[0][x]))
    m_avg = np.mean(m_list)
    return m_avg

def prepare_m_hist_details(table):
    # Расет значений m и подготовка списка с значениями по всей выборке
    m_list = []
    # Подготовка данных для расчета (импорт из таблицы)
    data_calc = prepare_two_row_data('POR', 'FF', table)
    for x in range(len(data_calc[0])):
        m_list.append(math.log(1 / data_calc[1][x], data_calc[0][x]))
    count, bins = np.histogram(m_list)
    return count, bins