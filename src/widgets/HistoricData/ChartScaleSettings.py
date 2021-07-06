from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox


class ChartScaleSettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setup_gui()

    def setup_gui(self):
        max_label = QLabel("Max")
        min_label = QLabel("Min")

        max_spin = QSpinBox()
        max_spin.valueChanged.connect(lambda value: self.max_spin_changed(value))
        min_spin = QSpinBox()
        min_spin.valueChanged.connect(lambda value: self.min_spin_changed(value))

        self.layout.addWidget(max_label)
        self.layout.addWidget(max_spin)
        self.layout.addWidget(min_label)
        self.layout.addWidget(min_spin)

    def max_spin_changed(self, value):
        self.parent().set_y_max_value(value)

    def min_spin_changed(self, value):
        self.parent().set_y_min_value(value)
