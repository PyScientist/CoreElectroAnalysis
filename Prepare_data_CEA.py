from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from PyQt5.QtCore import Qt

def convert_rows_to_columns(data_massive_to_convert):
    """
    Переформатирование рядов в колонки
    """
    data_massive_converted = []
    for y in range(len(data_massive_to_convert[0])):
        data_massive_converted.append([])
        for x in range(len(data_massive_to_convert)):
            data_massive_converted[y].append(data_massive_to_convert[x][y])
    return  data_massive_converted

def prepare_table_data_from_txt(path_to_data, delimeter = '\t', header_row = 1, units_row = 2):
    r"""
    функция prepare_table_data_from_txt Версия 1.0
    Подготовка табличных данных из txt файла с разделителем \t (знак табуляции) по умолчанию
    Получаем словарь состоящий из
    1) header - заголовки столбцов
    2) units - единицы измерений для столбцов
    3) data - двумерный список с данными типа [[n11, n12, ..., n1i], ..., [nj1, nj2, ..., nji]]
    где i - колличество строк в исходных данных, j - колличество столбцов в исходных данных
    Читается весь файл, то есть все не пустые строки, при этом выделяется заголовок и строка единиц измерений по умолчанию 1 и 2
    соответственно, но также строки могут быть заданны пользователем при вызове функции
    """
    data = []
    # Читаем файл
    input_file = open(path_to_data, 'r', encoding='utf-8')
    red_data = input_file.readlines()
    input_file.close()
    # Если файл содержит данные то перебираем строки
    if len(red_data) > 0:
        # Перебираем строки
        header = []
        units = []
        for line in range(len(red_data)):
            # Если встречаем строку с номером загоовка переносим ее в заголовок
            if line == header_row-1:
                header = (red_data[line].replace('\n','')).split(delimeter)
            # Если встречаем строку с номером строки едини.replace('\n','')ц измерений переносим ее в единицы измерения
            if line == units_row-1:
                units = (red_data[line].replace('\n','')).split(delimeter)
            # Если номер строки не совпадает с номером заголовка или номером строки единиц измерений
            # Добавляем данные из строки в массив данных
            if (line != header_row-1) and (line != units_row-1):
                data_line = (red_data[line].replace('\n','')).split(delimeter)
                # Если количество элементов в строке равно количеству заголовков то строку включаем
                if len(data_line) == len(header):
                    data.append(data_line)
                else:
                    print('Вероятно ошибка в строке: "'+str(data_line)+'" так как количество элементов в заголовке отличается от количества элементов в строке')
        data = convert_rows_to_columns(data)
        data_table = {'header': header, 'units': units, 'data': data}
        return data_table

def put_table_in_qtable_wiget(header, table_wiget, data):
    """
    Function to plot table (на вход список заголовков и данные таблицы) into QTableWidget
    При помещении таблицы в QTableWidget отдельно показываются заголовки (строка заголовков)
    Нумеруются ряды (крайняя левая колонка)
    """
    table_wiget.setRowCount(len(data[0]))  # Устанавливаем колличество рядов для таблицы
    table_wiget.setColumnCount(len(data))  # Устанавливаем колличество колонок для таблицы
    table_wiget.setHorizontalHeaderLabels(header)  # Устанавливаем в качестве заголовков список шапки
    # Создание заголовка для рядов
    row_header = []
    #for x in range(0, len(data[0])):
    #    row_header.append("row №" + str(x))
    #table_wiget.setVerticalHeaderLabels(row_header)  # Установка сформированного заголовка для рядов
    table_wiget.verticalHeader().setVisible(False)
    # Добавление данных в таблицу
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            table_wiget.setItem(y, x, QTableWidgetItem(str(data[x][y])))

def prepare_two_row_data(x_col_name, y_col_name, table):
    """
    Подготовка данных двух столбцов из табличного виджета QTableWidget по имени столбцов
    при возникновении ошибки функция возвращает пустой список иначе список со значениями требуемого ряда
    """
    column_one_container = []
    column_two_container = []
    x = None  # Изначально x не задан
    y = None  # Изначально y не задан
    for column in range(0, table.columnCount()): #Цикл перебор имен в шапке
        column_name = table.horizontalHeaderItem(column).text()
        if column_name == x_col_name:  # Если текст в колонке совпадает с названием требуемой колонки для переменной x
           x = column  # Присвоение номера колонки переменной x
        if column_name == y_col_name:  # Если текст в колонке совпадает с названием требуемой колонки для переменной y
           y = column  # Присвоение номера колонки переменной y
    try:
      for i in range(0, table.rowCount()):  # Перебираем ряды добовляя значения колонки с индексом x в список
          column_one_container.append(float(table.item(i, x).text()))
      for i in range(0, table.rowCount()):  # Перебираем ряды добовляя значения колонки с индексом y в список
          column_two_container.append(float(table.item(i, y).text()))
      return column_one_container, column_two_container
    except:
      return column_one_container, column_two_container

def modify_cells(TableWidget):
    '''
    Модифицируем ячейки таблицы и растягиваем их
    '''
    for row in range(TableWidget.rowCount()):
        for column in range(TableWidget.columnCount()):
            TableWidget.item(row, column).setTextAlignment(Qt.AlignCenter)
    TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)