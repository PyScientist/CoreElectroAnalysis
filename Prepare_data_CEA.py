from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QListWidgetItem

from PyQt5.QtCore import Qt

def mnemonics_adjustments(headers):
    """Mnemonics adjustments in header according chosen aliases"""

    # Mnemonic dictionary setup
    mnemonics_dict = {'POR': ['POR','Кп','Porosity','Open porosity','Por.'],
                      'RT' : ['RT','Resistivity','УЭС'],
                      'FF': ['FF', 'Рп', 'Formation Factor', 'Параметр пористости'],
                      'ZONE': ['FORMATION', 'PLAST', 'ZONE', 'Пласт', 'Зона'],
                      'WELL': ['WELL', 'скв.', 'скважина', 'номер скважины'],
                      'NLAB': ['NLAB', 'номер образца', 'образец', 'laboratory namber'],
                      'LITH': ['LITH', 'литотип', 'петротип', 'PETROTYPE'],
                      'RW' : ['RW', 'Water Resistivity']}

    for header in range(len(headers)):  # manipulating headers
        for alias in mnemonics_dict.keys():  # manipulating aliases
            for id in range(len(mnemonics_dict[alias])):  # manipulating mnemonics
                # if mnemonic matches the initial header then header mnemonic changes to alias
                if headers[header] == mnemonics_dict[alias][id]:
                    headers[header] = alias


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
    """Функция prepare_table_data_from_txt Версия 1.0
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
    """Function to plot table (на вход список заголовков и данные таблицы) into QTableWidget
    При помещении таблицы в QTableWidget отдельно показываются заголовки (строка заголовков)
    Нумеруются ряды (крайняя левая колонка)"""
    if len(data) == len(header):
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
    else:
        print(F'Imposible to load data due to ammount of headers {len(header)} differ from columns ammount {len(data)}')

def prepare_one_row_data(x_col_name, table):
    """Подготовка данных одного столбца из табличного виджета QTableWidget по имени столбца
    при возникновении ошибки функция возвращает пустой список иначе список со значениями требуемого ряда"""
    column_one_container = []
    x = None  # Изначально x не задан
    for column in range(0, table.columnCount()): #Цикл перебор имен в шапке
        column_name = table.horizontalHeaderItem(column).text()
        if column_name == x_col_name:  # Если текст в колонке совпадает с названием требуемой колонки для переменной x
           x = column  # Присвоение номера колонки переменной x
    try:
      for i in range(0, table.rowCount()):  # Перебираем ряды добовляя значения колонки с индексом x в список
          column_one_container.append(float(table.item(i, x).text()))
      return column_one_container
    except:
      return column_one_container

def prepare_two_row_data(x_col_name, y_col_name, table):
    """Подготовка данных двух столбцов из табличного виджета QTableWidget по имени столбцов
    при возникновении ошибки функция возвращает пустой список иначе список со значениями требуемого ряда"""
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


def get_data_from_QTableWidget(QTableWidget_input):
    header = []
    array = []
    for column in range(0, QTableWidget_input.columnCount()):
        header.append(QTableWidget_input.horizontalHeaderItem(column).text())
        temp_column = []
        for row in range(0, QTableWidget_input.rowCount()):
            temp_column.append(QTableWidget_input.item(row, column).text())
        array.append(temp_column)
    return header, array


def modify_cells(TableWidget):
    """Модифицируем ячейки таблицы и растягиваем их"""
    for row in range(TableWidget.rowCount()):
        for column in range(TableWidget.columnCount()):
            TableWidget.item(row, column).setTextAlignment(Qt.AlignCenter)
    TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def add_element_in_q_list_widget(list_widget, element):
    """Function which add item in list "QListWidget" the function obtains
    "item" and "QListWidget" instance where it is need to add "item"
    """
    item = QListWidgetItem()  # Create instance of list item for QListWidget
    item.setText(element)  # Set text for QListWidgetItem instance
    item.setCheckState(Qt.Checked)
    list_widget.addItem(item)  # Adding QListWidgetItem instance into the QListWidget


def set_uniq_data_to_listwidget(Table_obj, listwidget_obj, column_name):
    """Function to plo uniq values of parameter in corresponding ListWidget"""
    listwidget_obj.clear()
    unique = []
    for column in range(Table_obj.columnCount()):
        if Table_obj.horizontalHeaderItem(column).text() == column_name:
            for row in range(Table_obj.rowCount()):
                if unique.count(Table_obj.item(row, column).text()) < 1:
                    unique.append(Table_obj.item(row, column).text())

    for element in unique:
        add_element_in_q_list_widget(listwidget_obj, element)


def find_checked_categiries(list_w_wells, list_w_zones, list_w_lith):

    def process(list_w):
        list_checked = []
        for row in range(list_w.count()):
            if list_w.item(row).checkState() == Qt.Checked:
                list_checked.append(list_w.item(row).text())
        return list_checked

    return {'wells': process(list_w_wells), 'zones': process(list_w_zones), 'lith': process(list_w_lith)}


def row_filter_for_categories(checked_dict, table):

    well_column = None
    zone_column = None
    lith_column = None

    for column in range(table.columnCount()):
        column_name = table.horizontalHeaderItem(column).text()
        if column_name == 'WELL':
            well_column = column
        if column_name == 'ZONE':
            zone_column = column
        if column_name == 'LITH':
            lith_column = column

    row_to_exclude = []

    for row in range(table.rowCount()):
        if checked_dict['wells'].count(table.item(row, well_column).text()) < 1 or \
           checked_dict['zones'].count(table.item(row, zone_column).text()) < 1 or \
           checked_dict['lith'].count(table.item(row, lith_column).text()) < 1:
           row_to_exclude.append(row)

    if len(row_to_exclude) > 0:
        row_to_exclude.sort(reverse=True)

    return row_to_exclude