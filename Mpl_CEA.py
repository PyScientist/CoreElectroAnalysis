from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from matplotlib import pyplot as plt

import numpy as np

import math

from Prepare_data_CEA import prepare_two_row_data
from Calculations_CEA import prepare_m_hist_details

class MyMplCanavas(FigureCanvasQTAgg):
    '''
    Класс холста Qt для помещения рисунка Matplotlib
    '''
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)
        self.setMinimumSize(200,200)


def prepare_canvas_and_toolbar(layout = None):
    '''
    Функция для инициализации рисунка Matplotlib и его размещения в виджете Qt, добавления панели навигаии
    '''
    # Подготовка рисунка и осей
    fig, axes = plot_single_empty_graph()
    # Получение экземпляра класса холста с размещенным рисунком
    canvas = MyMplCanavas(fig)
    # Добавление виджета холста с рисунком в размещение
    layout.addWidget(canvas)
    # Добавление навигационной панели с привязкой к созданному холсту с рисунком Matplotlib
    toolbar = NavigationToolbar2QT(canvas, layout.parent())
    layout.addWidget(toolbar)
    return canvas, toolbar

def prepare_canvas(layout = None):
    '''
    Функция для инициализации рисунка Matplotlib и его размещения в виджете Qt
    '''
    # Подготовка рисунка и осей
    fig, axes = plot_single_empty_hist()
    # Получение экземпляра класса холста с размещенным рисунком
    canvas = MyMplCanavas(fig)
    # Добавление виджета холста с рисунком в размещение
    layout.addWidget(canvas)
    return canvas

def plot_single_empty_graph():
    '''
    Функция для подготовки рисунка с пустыми осями и предварительного их оформления, без задания данных
    '''
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85, facecolor='white', frameon=True, edgecolor='black', linewidth=1)
    fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Заголовок диаграммы рассеяния', fontsize=10)
    axes.set_xlabel('X', fontsize=8)
    axes.set_ylabel('Y', fontsize=8)
    return fig, axes

def plot_single_empty_hist():
    '''
    Функция для подготовки рисунка с пустыми осями и предварительного их оформления, без задания данных
    '''
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85, facecolor='white', frameon=True, edgecolor='black', linewidth=1)
    fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Заголовок гистограммы', fontsize=10)
    axes.set_xlabel('X', fontsize=8)
    axes.set_ylabel('Y', fontsize=8)
    return fig, axes

def plot_hist_of_m(table, axes):
    count, bins = prepare_m_hist_details(table)
    axes.hist(bins[:-1], bins, weights=count)
    axes.get_figure().canvas.draw()

def plot_m_mean_line(m_avg, axes):
    # Подготавливаем список с значениями пористости (Кп) с 0.01 до 1 с шагом 0.01 д.е.
    por_list = np.arange(0.01, 1.01, 0.01)
    # Рассчитываем список с значениями Рп изсходя из среднего значения m
    ri_clac_list = []
    for porosity in por_list:
        ri_clac_list.append(1 / (porosity ** m_avg))
    # Отображаем линию идллюстрирующую связь для среднего m на графике
    axes.plot(por_list, ri_clac_list, color='red')
    axes.get_figure().canvas.draw()

def plot_data_on_por_ff(table, axes):
    # Получаем из таблицы данные Кп и Рп для отображения на графике
    data_to_plot = prepare_two_row_data('POR', 'FF', table)

    # Отображаем данные и настраиваем внений вид графика
    axes.scatter(data_to_plot[0], data_to_plot[1])
    axes.set_title('Сопоставление Кп и Рп', fontsize=10)
    axes.set_xlabel('Кп, д.е.', fontsize=12)
    axes.set_ylabel('Pп', fontsize=12)
    axes.set_xlim(0.01, 1)
    axes.set_xscale('log')
    axes.set_ylim(1, 1000)
    axes.set_yscale('log')
    axes.get_figure().canvas.draw()

def plot_data_on_por_m(table, axes):
    # Расет значений m и подготовка списка с значениями по всей выборке
    m_list = []
    # Подготовка данных для расчета (импорт из таблицы)
    data_calc = prepare_two_row_data('POR', 'FF', table)
    for x in range(len(data_calc[0])):
        m_list.append(math.log(1 / data_calc[1][x], data_calc[0][x]))
    axes.scatter(data_calc[0], m_list)
    axes.set_title('Сопоставление Кп и m', fontsize=10)
    axes.set_xlabel('Кп, д.е.', fontsize=12)
    axes.set_ylabel('m', fontsize=12)
    axes.set_xlim(0, 0.4)
    axes.set_ylim(0, 5)
    axes.get_figure().canvas.draw()