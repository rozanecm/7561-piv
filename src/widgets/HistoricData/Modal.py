from typing import Dict

from PyQt5 import QtGui
from PyQt5.QtChart import QSplineSeries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QCheckBox
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

        self.markers = markers
        self.line_buttons = {}

        self.setMinimumWidth(250)

        self.set_gui()

    def set_gui(self):
        self.chart_settings_groupbox.setLayout(QVBoxLayout())
        for marker in self.markers:
            # current_marker = QCheckBox()
            current_marker = CheckBox(marker, parent=self)
            current_marker.setText(str(marker))
            self.line_buttons[marker] = current_marker
            self.chart_settings_groupbox.layout().addWidget(current_marker)
            # current_marker.stateChanged.connect(lambda: self.toggle(marker))
            # current_marker.clicked.connect(lambda: self.toggle(marker))
            # self.button.clicked.connect(lambda: self.process_csv_click())

    def toggle(self, marker: int, new_value: bool):
        self.parent().enable_line_toggle(marker, new_value)
