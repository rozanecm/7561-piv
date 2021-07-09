from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel, QSpinBox


class ModifyMarkersPositionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.set_gui()

    def set_gui(self):
        combo_box = QComboBox()
        combo_box.addItem("1")
        combo_box.addItem("2")
        combo_box.addItem("3")
        combo_box.addItem("4")

        self.layout.addWidget(combo_box)

        pos_x_label = QLabel("pos x")
        pos_x_spinbox = QSpinBox()
        pos_y_label = QLabel("pos y")
        pos_y_spinbox = QSpinBox()

        self.layout.addWidget(pos_x_label)
        self.layout.addWidget(pos_x_spinbox)
        self.layout.addWidget(pos_y_label)
        self.layout.addWidget(pos_y_spinbox)
