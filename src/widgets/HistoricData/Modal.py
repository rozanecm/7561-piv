from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.HistoricData.CheckBox import CheckBox
from src.widgets.HistoricData.typedef import line


class Modal(QDialog):
    def __init__(self, line_series: dict, parent=None):
        super(Modal, self).__init__(parent=parent)
        self.line_series: Dict[int, line] = {}

        self.setWindowModality(Qt.ApplicationModal)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.chart_settings_groupbox = GroupBox("Chart Settings")
        self.layout.addWidget(self.chart_settings_groupbox)
        self.right_side_layout = QVBoxLayout()
        delta_t_layout = QHBoxLayout()
        delta_t_label = QLabel("Delta t")
        delta_t_input = QSpinBox()
        delta_t_layout.addWidget(delta_t_label)
        delta_t_layout.addWidget(delta_t_input)

        ppm_layout = QHBoxLayout()
        ppm_label = QLabel("ppm")
        ppm_input = QSpinBox()
        ppm_layout.addWidget(ppm_label)
        ppm_layout.addWidget(ppm_input)

        self.right_side_layout.addLayout(delta_t_layout)
        self.right_side_layout.addLayout(ppm_layout)
        self.layout.addLayout(self.right_side_layout)

        self.line_series = line_series
        self.line_buttons = {}

        self.setMinimumWidth(300)

        self.set_gui()

    def set_gui(self):
        self.chart_settings_groupbox.setLayout(QVBoxLayout())
        for marker_id, value in self.line_series.items():
            current_marker = CheckBox(marker_id, parent=self)
            current_marker.setText(str(marker_id))
            self.line_buttons[marker_id] = current_marker
            self.chart_settings_groupbox.layout().addWidget(current_marker)
            current_marker.setChecked(value['is_visible'])

    def toggle(self, marker: int, new_value: bool):
        self.parent().enable_line_toggle(marker, new_value)
