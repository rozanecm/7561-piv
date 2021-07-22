from PyQt5.QtWidgets import QVBoxLayout, QSpinBox

from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class ROISelectorWidget(GroupBox):
    def __init__(self, settings_bearer, parent=None):
        super().__init__("ROI", parent=parent)
        self.settings_bearer = settings_bearer
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.roi_input = QSpinBox()
        self.roi_input.valueChanged.connect(lambda: self.roi_update())
        self.roi_input.setValue(Constants.INIT_ROI_VALUE)

        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(self.roi_input)

    def roi_update(self):
        self.settings_bearer.update_settings(Constants.SETTINGS_ROI, self.roi_input.value())
