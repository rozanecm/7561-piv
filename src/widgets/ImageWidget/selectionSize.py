from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QButtonGroup, QHBoxLayout, QSpinBox

from src.InfoOutputter import InfoOutputter
from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class SelectionSizeWidget(GroupBox):
    def __init__(self, outputter: InfoOutputter, parent=None):
        super().__init__("Tamaño de selección", parent=parent)
        self.other_value_spinner = QSpinBox()
        self.outputter = outputter
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_group = QButtonGroup()

        self.init_gui()
        self.setMinimumWidth(200)

    def init_gui(self):
        self.radio_button_8x8 = QRadioButton("8x8")
        self.radio_button_16x16 = QRadioButton("16x16")
        self.radio_button_32x32 = QRadioButton("32x32")
        self.radio_button_other = QRadioButton("otro")
        self.layout.addWidget(self.radio_button_8x8)
        self.layout.addWidget(self.radio_button_16x16)
        self.layout.addWidget(self.radio_button_32x32)

        other_option_layout = QHBoxLayout()
        other_option_layout.addWidget(self.radio_button_other)
        other_option_layout.addWidget(self.other_value_spinner)
        self.other_value_spinner.setMinimum(2)
        self.other_value_spinner.valueChanged.connect(lambda val: self.other_value_spinner_changed(val))
        # self.layout.addWidget(radio_button_other)
        self.layout.addLayout(other_option_layout)

        self.radio_button_8x8.setChecked(True)
        self.outputter.transmit_message(Constants.MSG_TYPE_SELECTION_SIZE_UPDATE, self.radio_button_8x8.text())

        self.button_group.addButton(self.radio_button_8x8)
        self.button_group.addButton(self.radio_button_16x16)
        self.button_group.addButton(self.radio_button_32x32)
        self.button_group.addButton(self.radio_button_other)
        self.button_group.buttonPressed.connect(lambda button: self.button_pressed(button))
        # self.button_group.buttonClicked.connect(lambda button: self.button_pressed(button))

    def button_pressed(self, button: QRadioButton):
        if button.text() == "otro":
            value = self.other_value_spinner.value()
            self.outputter.transmit_message(Constants.MSG_TYPE_SELECTION_SIZE_UPDATE, f"{value}x{value}")
        else:
            self.outputter.transmit_message(Constants.MSG_TYPE_SELECTION_SIZE_UPDATE, button.text())

    def other_value_spinner_changed(self, val):
        self.radio_button_other.click()
