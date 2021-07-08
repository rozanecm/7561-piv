from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


# from src.widgets.ImageWidget.ImageWidget import ImageWidget


class CircleMarker(QLabel):
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

    def __init__(self, new_point_id: int, size: int = 20, parent=None):
        super().__init__(parent=parent)
        self.id = new_point_id
        self.setText(str(self.id))
        self.marker_size = size
        self.setFixedSize(size, size)
        self.setStyleSheet(CircleMarker.selected_style.format(str(size / 2)))
        self.setAlignment(QtCore.Qt.AlignCenter)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.setMouseTracking(True)

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        mapped_to_global = self.mapToGlobal(ev.pos())
        self.parent().update_position(self.id, mapped_to_global.x(), mapped_to_global.y())

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.setMouseTracking(False)

    def update_id(self, new_id: int):
        self.id = new_id
        self.setText(str(self.id))
