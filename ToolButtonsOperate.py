from PyQt5.QtGui import QIcon, QPixmap, QWindow

from PyQt5.QtWidgets import QToolButton

from PyQt5.QtCore import QSize

def add_icon_to_the_button(button=None, icon_path_voc=None):
    """Place the icon on the button (the link to the button and
    the vocabulary with path to the icon depends on Mode are input)"""
    icon = QIcon()
    mode_list = ['Selected', 'Disabled', 'Normal']
    for mode in mode_list:
       if mode in icon_path_voc:
           pixmap = QPixmap(icon_path_voc[mode])
           icon.addPixmap(pixmap, QIcon.Mode == mode, QIcon.State == 'On')
           print(icon_path_voc[mode])
    button.setIcon(icon)
    button.setIconSize(QSize(50,50))

class ButtonsSetPorosityMAnalysis:
    '''
    Tool Palette for adjustment Porosity-M plot
    '''
    def __init__(self, buttonLayout):
        self.tool_buttons = []

        self.Button_plot_porosity_m_function = QToolButton()
        self.Button_plot_porosity_m_function.setToolTip('create m=f(Por) relation')

        icon_path_voc = {'Normal' : './figures/function_creation_icon__Normal.png',
                         'Disabled': './figures/function_creation_icon__Selected.png'}

        add_icon_to_the_button(self.Button_plot_porosity_m_function, icon_path_voc)
        self.Button_plot_porosity_m_function.setObjectName('Button_plot_porosity_m_function')
        self.tool_buttons.append(self.Button_plot_porosity_m_function)

        buttonLayout.addWidget(self.Button_plot_porosity_m_function)


    def delete_buttons_set(self):
        self.Button_plot_porosity_m_function.setParent(None)
        del self.Button_plot_porosity_m_function