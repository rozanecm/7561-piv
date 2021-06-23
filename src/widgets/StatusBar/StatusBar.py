from PyQt5.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    style = """background-color: {}; border-radius: 5px; text-align: right"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(self.style.format("gray"))

    def set_positive_message(self, msg: str):
        self.setStyleSheet(self.style.format("green"))
        self.showMessage(msg)

    def set_negative_message(self, msg: str):
        self.setStyleSheet(self.style.format("red"))
        self.showMessage(msg)

    def set_neutral_message(self, msg: str):
        self.setStyleSheet(self.style.format("gray"))
        self.showMessage(msg)
