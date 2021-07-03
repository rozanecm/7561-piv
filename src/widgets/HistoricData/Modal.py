from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QCheckBox

from src.widgets.GroupBox.GroupBox import GroupBox


class Modal(QDialog):
    def __init__(self, markers: list, parent=None):
        super(Modal, self).__init__(parent=parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chart_settings_groupbox = GroupBox("Chart Settings")
        self.layout.addWidget(self.chart_settings_groupbox)

        self.markers = markers

        self.setMinimumWidth(250)

        self.set_gui()

    def set_gui(self):
        self.chart_settings_groupbox.setLayout(QVBoxLayout())
        for marker in self.markers:
            current_marker = QCheckBox()
            current_marker.setText(str(marker))
            print(self.chart_settings_groupbox.layout())
            self.chart_settings_groupbox.layout().addWidget(current_marker)
