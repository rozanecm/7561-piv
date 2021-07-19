from PyQt5.QtWidgets import QHBoxLayout, QPushButton

from src.widgets.GroupBox.GroupBox import GroupBox


class TransportWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Transporte", parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(QPushButton())
        self.layout.addWidget(QPushButton())
        self.layout.addWidget(QPushButton())
