from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QToolButton, QWidget

from PyQt5.QtCore import QSize


class AbstractButtonForPallet(QToolButton):
    def __init__(self, path, tooltip, objectname, button_set, application):
        super().__init__()
        size = [50,50]
        icon = QIcon()
        pixmap = QPixmap(path)
        icon.addPixmap(pixmap)
        self.setIcon(icon)

        self.setIconSize(QSize(size[0], size[1]))
        self.setToolTip(tooltip)
        self.setObjectName(objectname)
        button_set.append(self)


class ButtonsSetForPorosityMAnalysis():
    """Tools Palette for adjustment Porosity-M plot"""
    def __init__(self, button_layout, parent):
        self.setObjectName = 'ButtonsSetForPorosityMAnalysis'
        self.tool_buttons = []

        AbstractButtonForPallet(path='./figures/function_creation_icon__Normal.png',
                                tooltip='create m=f(Por) relation',
                                objectname='Button_plot_porosity_m_function',
                                button_set = self.tool_buttons,
                                application=parent)

        AbstractButtonForPallet(path='./figures/results_icon.png',
                                tooltip='add m values to the table',
                                objectname='Button_add_m_value',
                                button_set = self.tool_buttons,
                                application=parent)

        AbstractButtonForPallet(path='./figures/select_dots.png',
                                tooltip='select points on the graph',
                                objectname='Button_Select_dots',
                                button_set = self.tool_buttons,
                                application=parent)

        AbstractButtonForPallet(path='./figures/Distributions.png',
                                tooltip='plot confidence interval',
                                objectname='Button_Distributions',
                                button_set = self.tool_buttons,
                                application=parent)

        for button in self.tool_buttons:
            button_layout.addWidget(button)

    def delete_buttons_set(self):
        def delete_single(button):
            button.setParent(None)
            del button

        for button in self.tool_buttons:
            delete_single(button)



