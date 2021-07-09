from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel, QSpinBox, QStyle

from src.widgets.GroupBox.GroupBox import GroupBox


class ModifyMarkersPositionWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Actualizar posición", parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setMinimumHeight(75)

        self.set_gui()

    def set_gui(self):
        marker_selector_label = QLabel("Punto:")
        self.layout.addWidget(marker_selector_label)

        marker_selector_combo_box = QComboBox()
        marker_selector_combo_box.textActivated.connect(lambda x: self.update_combo_box_value(x))
        marker_selector_combo_box.addItem("1")
        marker_selector_combo_box.addItem("2")
        marker_selector_combo_box.addItem("3")
        marker_selector_combo_box.addItem("4")
        self.layout.addWidget(marker_selector_combo_box)

        self.layout.addStretch()

        pos_x_label = QLabel("pos x")
        pos_x_spinbox = QSpinBox()
        pos_x_spinbox.valueChanged.connect(lambda value: self.pos_x_spin_changed(value))
        pos_y_label = QLabel("pos y")
        pos_y_spinbox = QSpinBox()
        pos_y_spinbox.valueChanged.connect(lambda value: self.pos_y_spin_changed(value))

        self.layout.addWidget(pos_x_label)
        self.layout.addWidget(pos_x_spinbox)
        self.layout.addWidget(pos_y_label)
        self.layout.addWidget(pos_y_spinbox)

    def update_combo_box_value(self, text):
        print(text)

    def pos_x_spin_changed(self, new_value):
        print(new_value)

    def pos_y_spin_changed(self, new_value):
        print(new_value)
