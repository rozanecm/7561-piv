import os
from typing import Dict

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from src.widgets.CircleMarker.CircleMarker import CircleMarker


class Image(QWidget):
    _img_width = 1344
    _img_height = 1024

    def __init__(self, main_window, parent=None):
        super().__init__(parent=parent)
        self.markers: Dict[int, CircleMarker] = {}
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/sample_cropped.png"))
        self.imageLabel = QLabel()
        self.set_image(path)
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.imageLabel)
        self.setLayout(self.layout)

        self.imageLabel.mouseDoubleClickEvent = self.process_double_click_on_img

    def set_image(self, path):
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled    # noqa: E501
        self.imageLabel.pixmap()
        self.imageLabel.logicalDpiX()
        self.imageLabel.setPixmap(QPixmap(path).scaled(self.imageLabel.size().width(),
                                                       self.imageLabel.size().height(),
                                                       QtCore.Qt.KeepAspectRatio))

    def process_double_click_on_img(self, event: QtGui.QMouseEvent) -> None:
        pos_in_global = self.imageLabel.mapToGlobal(event.pos())
        # this add point invokes the main window, which will handle all needed to create a new marker, like the id.
        self.main_window.add_point(pos_in_global.x(), pos_in_global.y())

    def add_point(self, x, y, new_point_id: int):
        # x, y are coords. taken with global reference.
        # we now have to paint the markers on the img.
        # so now we have to translate from global to self.
        new_pos = self.mapFromGlobal(QPoint(x, y))
        new_point = CircleMarker(new_point_id, parent=self)
        new_point.move(new_pos.x() - new_point.marker_size // 2,
                       new_pos.y() - new_point.marker_size // 2)
        new_point.show()
        self.markers[new_point_id] = new_point
        self.update()

    def update_position(self, point_id: int, new_x: int, new_y: int):
        current_marker = self.markers.get(point_id)
        new_x = new_x - current_marker.marker_size // 2
        new_y = new_y - current_marker.marker_size // 2
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)
            self.parentWidget().parent().update_position_from_image(point_id, new_x, new_y)

    def update_position_from_tab(self, point_id: int, new_x: int, new_y: int):
        current_marker = self.markers.get(point_id)
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)

    def point_on_image(self, x: int, y: int):
        return self.imageLabel.pixmap().width() >= x >= 0 and self.imageLabel.pixmap().height() >= y >= 0

    def remove_marker(self, marker_id: int):
        self.markers[marker_id].hide()
        del self.markers[marker_id]
        l1 = [x + 1 for x in range(len(self.markers.keys()))]
        l2 = list(self.markers.values())
        self.markers = dict(zip(l1, l2))
        for key, marker in self.markers.items():
            marker.update_id(key)
