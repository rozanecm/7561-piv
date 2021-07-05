from typing import Dict

from PyQt5.QtChart import QSplineSeries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from typing_extensions import TypedDict

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.HistoricData.CheckBox import CheckBox


class Modal(QDialog):
    def __init__(self, markers: dict, parent=None):
        super(Modal, self).__init__(parent=parent)
        line = TypedDict('line', {'is_visible': bool, 'series': QSplineSeries})
        self.line_series: Dict[int, line] = {}

        self.setWindowModality(Qt.ApplicationModal)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chart_settings_groupbox = GroupBox("Chart Settings")
        self.layout.addWidget(self.chart_settings_groupbox)

        self.line_series = markers
        self.line_buttons = {}

        self.setMinimumWidth(250)

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
