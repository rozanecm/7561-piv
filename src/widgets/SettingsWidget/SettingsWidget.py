from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpinBox, QLabel

from src.widgets.GroupBox.GroupBox import GroupBox


class SettingsWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración", parent=parent)
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.delta_t_layout = QHBoxLayout()
        self.delta_t_input = QSpinBox()
        delta_t_label = QLabel("Delta t")
        self.delta_t_layout.addWidget(delta_t_label)
        self.delta_t_layout.addWidget(self.delta_t_input)

        self.ppm_layout = QHBoxLayout()
        self.ppm_input = QSpinBox()
        ppm_label = QLabel("ppm")
        self.ppm_layout.addWidget(ppm_label)
        self.ppm_layout.addWidget(self.ppm_input)

        self.layout.addStretch()
        self.layout.addLayout(self.delta_t_layout)
        self.layout.addLayout(self.ppm_layout)
        self.layout.addStretch()

        self.setMinimumWidth(150)
