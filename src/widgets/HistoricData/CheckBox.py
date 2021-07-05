from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self, line_id: int, parent=None):
        super().__init__(parent=parent)
        self.line_id = line_id
        self.parent = parent
        self.stateChanged.connect(lambda: self.toggle())

    def toggle(self):
        self.parent.toggle(self.line_id, self.isChecked())
