from PyQt5 import QtGui
from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self, line_id: int, parent=None):
        super().__init__(parent=parent)
        self.line_id = line_id
        # self.stateChanged.
        self.parent = parent
        self.stateChanged.connect(lambda: self.toggle())

    def toggle(self):
        self.parent.toggle(self.line_id, self.isChecked())
