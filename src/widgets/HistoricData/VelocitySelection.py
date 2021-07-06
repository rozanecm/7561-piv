from PyQt5.QtWidgets import QHBoxLayout, QComboBox

from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class VelocitySelectionWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Selección de velocidad", parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.set_gui()

    def set_gui(self):
        combo_box = QComboBox()
        combo_box.addItem(Constants.VELOCITY_MAGNITUDE)
        combo_box.addItem(Constants.VELOCITY_VECT_X)
        combo_box.addItem(Constants.VELOCITY_VECT_Y)

        combo_box.textActivated.connect(lambda x: self.update_value(x))

        self.layout.addWidget(combo_box)

    def update_value(self, val):
        self.parent().change_velocity_type(val)
