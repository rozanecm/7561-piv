from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


class CircleMarker(QLabel):
    id = 0
    selected_style = """
            border: 3px solid red;
            color: black;
            background-color: red;
            border-radius: {0};
            """
    default_style = """
                border: 3px solid white;
                color: black;
                background-color: white;
                border-radius: {0};
                """

    def __init__(self, number: int, size: int = 20, parent=None):
        super().__init__(parent=parent)
        self.id = self.get_id()
        self.setText(str(number))
        print(size)
        self.setFixedSize(size, size)
        self.setStyleSheet(CircleMarker.selected_style.format(str(size / 2)))
        self.setAlignment(QtCore.Qt.AlignCenter)

    def get_id(self):
        CircleMarker.id += 1
        return CircleMarker.id

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        print("Marker with id {} clicked".format(self.id))
