from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QToolButton, \
                            QWidget,\
                            QHeaderView

from PyQt5.QtCore import QSize

from Prepare_data_CEA import get_data_from_QTableWidget,\
                             put_table_in_qtable_wiget,\
                             convert_rows_to_columns,\
                             modify_cells


from Calculations_CEA import prepare_m_list


class AbstractButtonForPallet(QToolButton):
    def __init__(self, path, tooltip, object_name, button_set, application):
        super().__init__()
        size = [50,50]
        self.setIcon(QIcon(QPixmap(path)))

        self.setIconSize(QSize(size[0], size[1]))
        self.setToolTip(tooltip)
        self.setObjectName(object_name)
        button_set.append(self)


class ButtonsSetForPorosityMAnalysis():
    """Tools Palette for adjustment Porosity-M plot"""
    def __init__(self, button_layout, parent):
        self.setObjectName = 'ButtonsSetForPorosityMAnalysis'
        self.tool_buttons = []
        self.parent = parent

        AbstractButtonForPallet(path='./figures/function_creation_icon__Normal.png',
                                tooltip='create m=f(Por) relation',
                                object_name='Button_plot_porosity_m_function',
                                button_set = self.tool_buttons,
                                application=self.parent)

        AbstractButtonForPallet(path='./figures/results_icon.png',
                                tooltip='add m values to the table',
                                object_name='Button_add_m_value',
                                button_set = self.tool_buttons,
                                application=self.parent)

        AbstractButtonForPallet(path='./figures/select_dots.png',
                                tooltip='select points on the graph',
                                object_name='Button_Select_dots',
                                button_set = self.tool_buttons,
                                application=self.parent)

        AbstractButtonForPallet(path='./figures/Distributions.png',
                                tooltip='plot confidence interval',
                                object_name='Button_Distributions',
                                button_set = self.tool_buttons,
                                application=self.parent)

        for button in self.tool_buttons:
            button_layout.addWidget(button)
            # Prepare signals for buttons
            if button.objectName() == 'Button_add_m_value':
                button.clicked.connect(self.Button_add_m_value_clicked)

    def Button_add_m_value_clicked(self):

        header, array = get_data_from_QTableWidget(self.parent.InitDataTable)
        m_list = prepare_m_list(self.parent.InitDataTable)
        header.append('m')
        array.append(m_list)

        put_table_in_qtable_wiget(header, self.parent.InitDataTable, array)
        modify_cells(self.parent.InitDataTable)







    def delete_buttons_set(self):
        def delete_single(button):
            button.setParent(None)
            del button

        for button in self.tool_buttons:
            delete_single(button)



