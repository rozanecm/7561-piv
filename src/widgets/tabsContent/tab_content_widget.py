from PyQt5.QtWidgets import QWidget

from src.widgets.tabsContent.tab_content import Ui_TabContent


class TabContent(QWidget, Ui_TabContent):
    def __init__(self, parent=None, position_x: int = 100, position_y: int = 100):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.x32_radioButton.setChecked(True)
        self.pos_x_spinBox.setValue(position_x)
        self.pos_y_spinBox.setValue(position_y)

    def update_position(self, new_x: int, new_y: int):
        self.pos_x_spinBox.setValue(new_x)
        self.pos_y_spinBox.setValue(new_y)

    def update_position_x(self, new_x):
        print("updating x position from tab content widget to: ", new_x)

    def update_position_y(self, new_y):
        print("updating y position from tab content widget to: ", new_y)
