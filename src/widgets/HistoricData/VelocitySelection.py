from PyQt5.QtWidgets import QHBoxLayout, QComboBox

from src.widgets.GroupBox.GroupBox import GroupBox


class VelocitySelectionWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Selección de velocidad", parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(QComboBox())
