from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QLabel, QSpinBox

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class ModifyMarkersPositionWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Actualizar posición de puntos", parent=parent)
        self.marker_selector_combo_box = QComboBox()
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
        self.pos_x_spinbox.editingFinished.connect(lambda: self.spinbox_value_changed())
        pos_y_label = QLabel("pos y")
        self.pos_y_spinbox.setEnabled(False)
        self.pos_y_spinbox.setMaximum(9999)
        self.pos_y_spinbox.editingFinished.connect(lambda: self.spinbox_value_changed())
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

    def spinbox_value_changed(self):
        marker_id = self.marker_selector_combo_box.currentText()
        if marker_id:
            x = self.pos_x_spinbox.value()
            y = self.pos_y_spinbox.value()
            self.parent().update_position_from_marker_position_update_widget(int(marker_id), x, y)

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

    def remove_marker(self, marker_id: int):
        self.empty_combobox()
        del self.markers[str(marker_id)]
        self.reorder_markers()
        self.repopulate_combobox()
        if self.markers:
            self.update_combo_box_value()
        else:
            self.pos_x_spinbox.setValue(0)
            self.pos_y_spinbox.setValue(0)

    def empty_combobox(self):
        for key in self.markers.keys():
            self.marker_selector_combo_box.removeItem(self.marker_selector_combo_box.findText(key))

    def repopulate_combobox(self):
        for key in self.markers.keys():
            self.marker_selector_combo_box.addItem(str(key))

    def reorder_markers(self):
        l1 = [str(x + 1) for x in range(len(self.markers.keys()))]
        l2 = list(self.markers.values())
        self.markers = dict(zip(l1, l2))

    def update_marker_position_from_main_window(self, marker_id: int, pos: tuple):
        """receive x, y in img coordinates"""
        self.markers[str(marker_id)] = pos
        if self.marker_selector_combo_box.currentText() == str(marker_id):
            self.update_combo_box_value()

    def set_min_max_x_value(self, min: int, max: int):
        self.pos_x_spinbox.setMinimum(min)
        self.pos_x_spinbox.setMaximum(max)

    def set_min_max_y_value(self, min: int, max: int):
        self.pos_y_spinbox.setMinimum(min)
        self.pos_y_spinbox.setMaximum(max)
