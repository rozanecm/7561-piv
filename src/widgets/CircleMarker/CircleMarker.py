from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


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
        print("Marker with id {} clicked".format(self.id))
        self.setMouseTracking(True)

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        mapped_to_parent = self.mapToParent(ev.pos())
        print("original pos: {}; mapped to parent: {}".format(ev.pos(), mapped_to_parent))
        self.parent().update_position(self.id, mapped_to_parent.x(), mapped_to_parent.y())

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.setMouseTracking(False)
