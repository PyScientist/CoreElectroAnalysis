from PyQt5.QtGui import QIcon, QPixmap, QWindow

from PyQt5.QtWidgets import QToolButton

from PyQt5.QtCore import QSize


class AbstractButtonForPallet(QToolButton):
    def __init__(self, path, tooltip, objectName, button_set, application):
        super().__init__()
        size = [50,50]
        icon = QIcon()
        pixmap = QPixmap(path)
        icon.addPixmap(pixmap)
        self.setIcon(icon)

        self.setIconSize(QSize(size[0], size[1]))
        self.setToolTip(tooltip)
        self.setObjectName(objectName)
        button_set.append(self)


class ButtonsSetForPorosityMAnalysis:
    """Tools Palette for adjustment Porosity-M plot"""
    def __init__(self, button_layout, parent):
        self.tool_buttons = []

        self.Button_plot_porosity_m_function = AbstractButtonForPallet(path='./figures/function_creation_icon__Normal.png',
                                                                       tooltip='create m=f(Por) relation',
                                                                       objectName='Button_plot_porosity_m_function',
                                                                       button_set = self.tool_buttons,
                                                                       application=parent)

        self.Button_add_m_value = AbstractButtonForPallet(path='./figures/results_icon.png',
                                                          tooltip='add m values to the table',
                                                          objectName='Button_add_m_value',
                                                          button_set = self.tool_buttons,
                                                          application=parent)

        self.Button_Select_dots = AbstractButtonForPallet(path='./figures/select_dots.png',
                                                          tooltip='select points on the graph',
                                                          objectName='Button_Select_dots',
                                                          button_set = self.tool_buttons,
                                                          application=parent)

        self.Button_Distributions = AbstractButtonForPallet(path='./figures/Distributions.png',
                                                            tooltip='plot confidence interval',
                                                            objectName='Button_Distributions',
                                                            button_set = self.tool_buttons,
                                                            application=parent)

        for button in self.tool_buttons:
            button_layout.addWidget(button)


    def delete_buttons_set(self):
        def delete_single(button):
            button.setParent(None)
            del button

        for button in self.tool_buttons:
            print(button.objectName())
            if hasattr(self, F'{button.objectName()}'):
               delete_single(button)

