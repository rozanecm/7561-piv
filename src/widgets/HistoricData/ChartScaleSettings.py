from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSpinBox

from src.widgets.GroupBox.GroupBox import GroupBox


def create_spinbox(func):
    spin = QSpinBox()
    spin.valueChanged.connect(lambda value: func(value))
    spin.setMinimum(-9999)
    spin.setMaximum(9999)
    return spin


class ChartScaleSettingsWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Escala eje Y", parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setup_gui()

    def setup_gui(self):
        self.layout.addWidget(QLabel("Min"))
        self.layout.addWidget(create_spinbox(self.min_spin_changed))
        self.layout.addWidget(QLabel("Max"))
        self.layout.addWidget(create_spinbox(self.max_spin_changed))

    def max_spin_changed(self, value):
        self.parent().set_y_max_value(value)

    def min_spin_changed(self, value):
        self.parent().set_y_min_value(value)
