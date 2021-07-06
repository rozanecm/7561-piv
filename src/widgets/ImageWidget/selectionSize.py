from PyQt5.QtWidgets import QVBoxLayout, QRadioButton

from src.widgets.GroupBox.GroupBox import GroupBox


class SelectionSizeWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Tamaño de selección", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_gui()
        self.setMinimumWidth(200)

    def init_gui(self):
        self.layout.addWidget(QRadioButton("8x8"))
        self.layout.addWidget(QRadioButton("16x16"))
        self.layout.addWidget(QRadioButton("32x32"))
        self.layout.addWidget(QRadioButton("otro"))
