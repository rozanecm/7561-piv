from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpinBox, QLabel

from src.widgets.GroupBox.GroupBox import GroupBox


class SettingsWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración", parent=parent)
        self.setMinimumWidth(150)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.delta_t_input = QSpinBox()
        self.ppm_input = QSpinBox()

        self.layout.addStretch()
        self.setup_delta_t()
        self.setup_ppm()
        self.layout.addStretch()

    def setup_ppm(self):
        ppm_layout = QHBoxLayout()
        ppm_label = QLabel("ppm")
        ppm_layout.addWidget(ppm_label)
        ppm_layout.addWidget(self.ppm_input)
        self.layout.addLayout(ppm_layout)

    def setup_delta_t(self):
        delta_t_layout = QHBoxLayout()
        delta_t_label = QLabel("Delta t")
        delta_t_layout.addWidget(delta_t_label)
        delta_t_layout.addWidget(self.delta_t_input)
        self.layout.addLayout(delta_t_layout)
