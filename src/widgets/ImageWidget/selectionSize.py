from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QButtonGroup, QHBoxLayout, QSpinBox

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


def selection_size_as_int(selection_size_text: str) -> int:
    return int(selection_size_text.split("x")[0])


class SelectionSizeWidget(GroupBox):
    def __init__(self, settings_bearer: SettingsBearer, main_window, parent=None):
        # parent: imageWidget
        super().__init__("Tamaño de selección", parent=parent)
        self.main_window = main_window
        self.setMinimumWidth(200)
        self.settings_bearer = settings_bearer
        self.parent = parent

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.radio_button_other = QRadioButton("otro")
        self.radio_button_32x32 = QRadioButton("32x32")
        self.radio_button_16x16 = QRadioButton("16x16")
        self.radio_button_8x8 = QRadioButton("8x8")
        self.other_value_spinner = QSpinBox()

        self.button_group = QButtonGroup()

        self.init_gui()

    def init_gui(self):
        self.set_numeric_radio_buttons()
        self.set_other_size_radio_button()
        self.initial_radio_button_check()
        self.setup_button_group()

    def setup_button_group(self):
        self.button_group.addButton(self.radio_button_8x8)
        self.button_group.addButton(self.radio_button_16x16)
        self.button_group.addButton(self.radio_button_32x32)
        self.button_group.addButton(self.radio_button_other)
        self.button_group.buttonPressed.connect(lambda button: self.button_pressed(button))

    def initial_radio_button_check(self):
        self.radio_button_8x8.setChecked(True)
        self.settings_bearer.update_settings(Constants.SETTINGS_SELECTION_SIZE,
                                             selection_size_as_int(self.radio_button_8x8.text().split("x")[0]))
        self.parent.roi_selector_widget.set_min_value()

    def set_other_size_radio_button(self):
        other_option_layout = QHBoxLayout()
        other_option_layout.addWidget(self.radio_button_other)
        other_option_layout.addWidget(self.other_value_spinner)
        self.other_value_spinner.setMinimum(2)
        self.other_value_spinner.valueChanged.connect(lambda val: self.other_value_spinner_changed(val))
        self.layout.addLayout(other_option_layout)

    def set_numeric_radio_buttons(self):
        self.layout.addWidget(self.radio_button_8x8)
        self.layout.addWidget(self.radio_button_16x16)
        self.layout.addWidget(self.radio_button_32x32)

    def button_pressed(self, button: QRadioButton):
        if button.text() == "otro":
            value = self.other_value_spinner.value()
            self.settings_bearer.update_settings(Constants.SETTINGS_SELECTION_SIZE,
                                                 value)
        else:
            self.settings_bearer.update_settings(Constants.SETTINGS_SELECTION_SIZE,
                                                 selection_size_as_int(button.text()))
        self.parent.roi_selector_widget.set_min_value()
        self.main_window.check_if_markers_margin_is_not_exceeding_imgs_limits()

    def other_value_spinner_changed(self, val):
        self.radio_button_other.click()
