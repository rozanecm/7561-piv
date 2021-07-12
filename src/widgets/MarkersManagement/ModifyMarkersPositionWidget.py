from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QLabel, QSpinBox

from src.InfoOutputter import InfoOutputter
from src.widgets.GroupBox.GroupBox import GroupBox


class ModifyMarkersPositionWidget(GroupBox):
    def __init__(self, outputter: InfoOutputter, parent=None):
        super().__init__("Actualizar posición de puntos", parent=parent)
        self.marker_selector_combo_box = QComboBox()
        self.outputter = outputter
        self.pos_y_spinbox = QSpinBox()
        self.pos_x_spinbox = QSpinBox()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.markers = {}

        self.setMinimumHeight(75)

        self.set_gui()

    def set_gui(self):
        self.setup_marker_selector()

        self.layout.addStretch()

        self.setup_spinboxes()

    def setup_spinboxes(self):
        pos_x_label = QLabel("pos x")
        self.pos_x_spinbox.setEnabled(False)
        self.pos_x_spinbox.setMaximum(9999)
        self.pos_x_spinbox.valueChanged.connect(lambda value: self.pos_x_spin_changed(value))
        pos_y_label = QLabel("pos y")
        self.pos_y_spinbox.setEnabled(False)
        self.pos_y_spinbox.setMaximum(9999)
        self.pos_y_spinbox.valueChanged.connect(lambda value: self.pos_y_spin_changed(value))
        self.layout.addWidget(pos_x_label)
        self.layout.addWidget(self.pos_x_spinbox)
        self.layout.addWidget(pos_y_label)
        self.layout.addWidget(self.pos_y_spinbox)

    def setup_marker_selector(self):
        marker_selector_label = QLabel("Punto:")
        self.layout.addWidget(marker_selector_label)
        self.marker_selector_combo_box.textActivated.connect(lambda x: self.update_combo_box_value(x))
        self.layout.addWidget(self.marker_selector_combo_box)

    def update_combo_box_value(self, text=""):
        self.pos_x_spinbox.setValue(self.markers[self.marker_selector_combo_box.currentText()][0])
        self.pos_y_spinbox.setValue(self.markers[self.marker_selector_combo_box.currentText()][1])

    def pos_x_spin_changed(self, new_value):
        print(new_value)

    def pos_y_spin_changed(self, new_value):
        print(new_value)

    def enable_spinboxes(self):
        self.pos_x_spinbox.setEnabled(True)
        self.pos_y_spinbox.setEnabled(True)

    def disable_spinboxes(self):
        self.pos_x_spinbox.setEnabled(False)
        self.pos_y_spinbox.setEnabled(False)

    def add_marker(self, marker_id: int, position: tuple):
        self.marker_selector_combo_box.addItem(str(marker_id))
        self.markers[str(marker_id)] = position
        self.update_combo_box_value()
