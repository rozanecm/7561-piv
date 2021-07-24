from PyQt5.QtWidgets import QVBoxLayout, QSpinBox

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class ROISelectorWidget(GroupBox):
    def __init__(self, settings_bearer: SettingsBearer, main_window, parent=None):
        super().__init__("ROI", parent=parent)
        self.settings_bearer = settings_bearer
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.roi_input = QSpinBox()
        self.roi_input.setMaximum(Constants.ROI_MAX_VALUE)
        self.roi_input.valueChanged.connect(lambda: self.roi_update())
        self.roi_input.setValue(Constants.INIT_ROI_VALUE)

        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(self.roi_input)

    def roi_update(self):
        self.settings_bearer.update_settings(Constants.SETTINGS_ROI, self.roi_input.value())

    def set_min_value(self):
        # 2 times the passed value is somewhat arbitrary:
        # the ROI should be n times bigger than the selection size because else the algorithm wouldn't make sense.
        # But the exact value that makes sense may differ.
        self.roi_input.setMinimum(2 * self.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE])
