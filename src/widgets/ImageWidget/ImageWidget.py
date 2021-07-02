import os
from typing import Dict

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from src.widgets.CircleMarker.CircleMarker import CircleMarker
from src.widgets.GroupBox.GroupBox import GroupBox


class ImageWidget(GroupBox):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    def __init__(self, parent=None):
        super().__init__("Image", parent=parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.image = Image(self.parent())

        self.layout.addStretch()
        self.layout.addWidget(self.image)
        self.layout.addStretch()

        self.show()


class Image(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent=parent)
        self.markers: Dict[int, CircleMarker] = {}
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/sample_cropped.png"))
        self.imageLabel = QLabel()
        self.set_image(path)
        self.main_window = main_window
        self.imageLabel.setStyleSheet("""border-color:red;
                border-style: solid;
                border-width: 5px;""")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.imageLabel)
        self.setLayout(self.layout)

    def set_image(self, path):
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled    # noqa: E501
        self.imageLabel.pixmap()
        self.imageLabel.logicalDpiX()
        self.imageLabel.setPixmap(
            QPixmap(path).scaled(self.imageLabel.size().width(), self.imageLabel.size().height(),
                                 QtCore.Qt.KeepAspectRatio))
        print("img label size:", self.imageLabel.size())
        print("pixmap size:", self.imageLabel.pixmap().size())

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        x = event.pos().x()
        y = event.pos().y()
        # this add point invokes the main window, which will handle all needed to create a new marker, like the id.
        self.main_window.add_point(x, y)
        print("img label size:", self.imageLabel.size())
        print("pixmap size:", self.imageLabel.pixmap().size())

    def add_point(self, x, y, new_point_id: int):
        new_point = CircleMarker(new_point_id, parent=self)
        new_point.move(x - new_point.marker_size // 2,
                       y - new_point.marker_size // 2)
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
