from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QCheckBox


class Modal(QDialog):
    def __init__(self, markers: list, parent=None):
        super(Modal, self).__init__(parent=parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.markers = markers

        self.set_gui()

    def set_gui(self):
        for marker in self.markers:
            current_marker = QCheckBox()
            current_marker.setText(str(marker))
            self.layout.addWidget(current_marker)
