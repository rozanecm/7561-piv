from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSpinBox

from src.widgets.GroupBox.GroupBox import GroupBox


def create_spinbox(func, init_value: int = 0):
    spin = QSpinBox()
    spin.setValue(init_value)
    spin.valueChanged.connect(lambda value: func(value))
    spin.setMinimum(-9999)
    spin.setMaximum(9999)
    return spin


class ChartScaleSettingsWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Escala eje Y", parent=parent)
        self.max_y_spinbox = create_spinbox(self.max_spin_changed, init_value=15)
        self.min_y_spinbox = create_spinbox(self.min_spin_changed)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setup_gui()

    def setup_gui(self):
        self.layout.addWidget(QLabel("Min"))
        self.layout.addWidget(self.min_y_spinbox)
        self.layout.addWidget(QLabel("Max"))
        self.layout.addWidget(self.max_y_spinbox)

    def max_spin_changed(self, value):
        self.parent().set_y_max_value(value)

    def min_spin_changed(self, value):
        self.parent().set_y_min_value(value)
