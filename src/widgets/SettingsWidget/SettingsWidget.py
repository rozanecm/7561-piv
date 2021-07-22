from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpinBox, QLabel

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class SettingsWidget(GroupBox):
    def __init__(self, settings_bearer: SettingsBearer, parent=None):
        super().__init__("Configuración", parent=parent)
        self.settings_bearer = settings_bearer
        self.setMinimumWidth(150)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.delta_t_input = QSpinBox()
        self.delta_t_input.valueChanged.connect(lambda: self.delta_t_update())
        self.ppm_input = QSpinBox()
        self.ppm_input.valueChanged.connect(lambda: self.ppm_update())

        self.layout.addStretch()
        self.setup_delta_t()
        self.setup_ppm()
        self.layout.addStretch()

    def setup_ppm(self):
        self.ppm_input.setValue(1)
        ppm_layout = QHBoxLayout()
        ppm_label = QLabel("px/mm:")
        ppm_layout.addWidget(ppm_label)
        ppm_layout.addWidget(self.ppm_input)
        self.layout.addLayout(ppm_layout)

    def setup_delta_t(self):
        self.delta_t_input.setValue(1)
        delta_t_layout = QHBoxLayout()
        delta_t_label = QLabel("Δ t:")
        delta_t_layout.addWidget(delta_t_label)
        delta_t_layout.addWidget(self.delta_t_input)
        self.layout.addLayout(delta_t_layout)

    def delta_t_update(self):
        self.settings_bearer.update_settings(Constants.SETTINGS_DELTA_T, self.delta_t_input.value())

    def ppm_update(self):
        self.settings_bearer.update_settings(Constants.SETTINGS_PPM, self.ppm_input.value())
