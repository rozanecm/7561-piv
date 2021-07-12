import os
from typing import Dict

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from src.InfoOutputter import InfoOutputter
from src.constants.constants import Constants
from src.widgets.CircleMarker.CircleMarker import CircleMarker


class Image(QWidget):
    _img_width = 1344
    _img_height = 1024

    def __init__(self, outputter: InfoOutputter, main_window, parent=None):
        super().__init__(parent=parent)
        self.outputter = outputter
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
        pos_in_image_label = self.imageLabel.mapFromGlobal(pos_in_global)
        x_real_img = round(pos_in_image_label.x() * self._img_width / self.imageLabel.width())
        y_real_img = round(pos_in_image_label.y() * self._img_height / self.imageLabel.height())
        self.main_window.add_point(pos_in_global.x(), pos_in_global.y(), x_real_img, y_real_img)

    def add_point(self, x, y, new_point_id: int):
        # x, y are coords. taken with global reference.
        # we now have to paint the markers on the img.
        # so now we have to translate from global to self.
        new_pos = self.mapFromGlobal(QPoint(x, y))
        new_point = CircleMarker(new_point_id,
                                 self.map_from_self_to_real_image_coordinates((new_pos.x(), new_pos.y())),
                                 parent=self)
        new_point.move(new_pos.x() - new_point.marker_size // 2,
                       new_pos.y() - new_point.marker_size // 2)
        new_point.update_position(self.map_from_self_to_real_image_coordinates(
            (new_pos.x() - new_point.marker_size // 2,
             new_pos.y() - new_point.marker_size // 2)))
        new_point.show()
        self.markers[new_point_id] = new_point
        self.update()

    def map_from_self_to_real_image_coordinates(self, coords_in_image_widget: tuple):
        return (round(coords_in_image_widget[0] * self._img_width / self.imageLabel.width()),
                round(coords_in_image_widget[1] * self._img_height / self.imageLabel.height()))

    def update_position(self, point_id: int, new_x: int, new_y: int):
        # new_x and new_y are expressed in global coords.
        # we should translate to self.imageLabel coords.
        current_marker = self.markers.get(point_id)
        translated_coords = self.mapFromGlobal(QPoint(new_x, new_y))
        new_x = translated_coords.x() - current_marker.marker_size // 2
        new_y = translated_coords.y() - current_marker.marker_size // 2
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)
            current_marker.update_position(self.map_from_self_to_real_image_coordinates((
                translated_coords.x() - current_marker.marker_size // 2,
                translated_coords.y() - current_marker.marker_size // 2)))

    def finish_position_update(self, point_id: int):
        self.outputter.transmit_message_dict(Constants.MSG_TYPE_UPDATE_MARKER,
                                             {"marker_id": point_id, "pox_x": self.markers[point_id].pos[0],
                                              "pos_y": self.markers[point_id].pos[1]})

    def update_position_from_tab(self, point_id: int, new_x: int, new_y: int):
        current_marker = self.markers.get(point_id)
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)

    def point_on_image(self, x: int, y: int):
        return self.imageLabel.pixmap().width() >= x >= 0 and self.imageLabel.pixmap().height() >= y >= 0

    def remove_marker(self, marker_id: int):
        self.outputter.transmit_message_dict(Constants.MSG_TYPE_DELETE_MARKER,
                                             {"marker_id": marker_id,
                                              "pos": self.markers[marker_id].pos})
        self.markers[marker_id].hide()
        del self.markers[marker_id]
        self.reorder_markers()
        self.main_window.remove_marker(marker_id)

    def reorder_markers(self):
        l1 = [x + 1 for x in range(len(self.markers.keys()))]
        l2 = list(self.markers.values())
        self.markers = dict(zip(l1, l2))
        for key, marker in self.markers.items():
            marker.update_id(key)
