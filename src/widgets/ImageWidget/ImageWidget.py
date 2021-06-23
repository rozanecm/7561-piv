from typing import Dict

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from src.widgets.CircleMarker.CircleMarker import CircleMarker


class ImageWidget(QWidget):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.markers: Dict[int, CircleMarker] = {}
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        path = "res/sample_cropped.png"

        self.imageLabel = QLabel()
        self.set_image(path)

        self.layout.addWidget(self.imageLabel)

        self.show()

    def set_image(self, path):
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled    # noqa: E501
        if self.imageLabel.size().width() > self.imageLabel.size().height():
            self.imageLabel.setPixmap(
                QPixmap(path).scaled(self.imageLabel.size().width(), self.imageLabel.size().width(),
                                     QtCore.Qt.KeepAspectRatio))
        else:
            self.imageLabel.setPixmap(
                QPixmap(path).scaled(self.imageLabel.size().width(), self.imageLabel.size().width(),
                                     QtCore.Qt.KeepAspectRatio))

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}; current size: {}".format(x, y, self.size()))
        print("widget size:", self.frameSize())
        self.parent().add_point(x, y)

    def add_point(self, x, y, new_point_id: int):
        new_point = CircleMarker(new_point_id, parent=self)
        new_point.move(x - new_point.marker_size // 2,
                       y - new_point.marker_size // 2)
        new_point.show()
        self.markers[new_point_id] = new_point
        self.update()

    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}".format(x, y))

    def update_position(self, point_id: int, new_x: int, new_y: int):
        current_marker = self.markers.get(point_id)
        new_x = new_x - current_marker.marker_size // 2
        new_y = new_y - current_marker.marker_size // 2
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)
            self.parentWidget().update_position_from_image(point_id, new_x, new_y)

    def update_position_from_tab(self, point_id: int, new_x: int, new_y: int):
        current_marker = self.markers.get(point_id)
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)

    def point_on_image(self, x: int, y: int):
        return self.imageLabel.pixmap().width() >= x >= 0 and self.imageLabel.pixmap().height() >= y >= 0
