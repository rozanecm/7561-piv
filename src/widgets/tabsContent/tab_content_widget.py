from PyQt5.QtWidgets import QWidget

from src.widgets.tabsContent.tab_content import Ui_TabContent


class TabContent(QWidget, Ui_TabContent):
    def __init__(self, main_window, point_id: int, parent=None, position_x: int = 100, position_y: int = 100):
        QWidget.__init__(self, parent=parent)
        self.main_window = main_window
        self.point_id = point_id
        self.setupUi(self)
        self.x32_radioButton.setChecked(True)
        self.unblock_spinbox_signals()
        self.pos_x_spinBox.setValue(position_x)
        self.pos_y_spinBox.setValue(position_y)
        self.block_spinbox_signals()

    def block_spinbox_signals(self):
        self.pos_x_spinBox.blockSignals(False)
        self.pos_y_spinBox.blockSignals(False)

    def unblock_spinbox_signals(self):
        self.pos_x_spinBox.blockSignals(True)
        self.pos_y_spinBox.blockSignals(True)

    def update_position(self, new_x: int, new_y: int):
        self.unblock_spinbox_signals()
        self.pos_x_spinBox.setValue(new_x)
        self.pos_y_spinBox.setValue(new_y)
        self.block_spinbox_signals()

    def update_position_x(self, new_x):
        self.main_window.update_position_from_tab(self.point_id, new_x, self.pos_y_spinBox.value())

    def update_position_y(self, new_y):
        self.main_window.update_position_from_tab(self.point_id, self.pos_x_spinBox.value(), new_y)
