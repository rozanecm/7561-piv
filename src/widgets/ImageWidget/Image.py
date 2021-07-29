import os
from typing import Dict

import PIL.Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.CircleMarker.CircleMarker import CircleMarker


def show_marker_manipulation_disabled_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Marcadores")
    text = "No se puedo insertar el marcador."
    informative_text = "Por favor, asegúrese de haber obtenido una previsualiazción y que el algoritmo no esté " \
                       "corriendo. "
    msg.setText("%s\n\n%s" % (text, informative_text))
    msg.exec()


class Image(QWidget):
    img_width = 1344
    img_height = 1024

    def __init__(self, settings_bearer: SettingsBearer, main_window, parent=None):
        super().__init__(parent=parent)
        self.settings_bearer = settings_bearer
        self.markers: Dict[int, CircleMarker] = {}
        self.can_manipulate_markers = False
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/preview.png"))
        self.imageLabel = QLabel()
        self.set_image_from_path(path)
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.imageLabel)
        self.setLayout(self.layout)

        self.imageLabel.mouseDoubleClickEvent = self.process_double_click_on_img

    def set_image_from_path(self, path):
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled    # noqa: E501
        self.imageLabel.setPixmap(QPixmap(path).scaled(self.imageLabel.size().width(),
                                                       self.imageLabel.size().height(),
                                                       QtCore.Qt.KeepAspectRatio,
                                                       QtCore.Qt.SmoothTransformation))

    def set_image_from_PIL(self, img: PIL.Image.Image):
        self.img_width = img.width
        self.img_height = img.height
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled    # noqa: E501
        self.imageLabel.setPixmap(QPixmap.fromImage(ImageQt(img)).scaled(self.imageLabel.size().width(),
                                                                         self.imageLabel.size().height(),
                                                                         QtCore.Qt.KeepAspectRatio,
                                                                         QtCore.Qt.SmoothTransformation))

    def process_double_click_on_img(self, event: QtGui.QMouseEvent) -> None:
        if self.can_manipulate_markers:
            pos_in_global = self.imageLabel.mapToGlobal(event.pos())
            # this add point invokes the main window, which will handle all needed to create a new marker, like the id.
            pos_in_image_label = self.imageLabel.mapFromGlobal(pos_in_global)
            x_real_img = round(pos_in_image_label.x() * self.img_width / self.imageLabel.width())
            y_real_img = round(pos_in_image_label.y() * self.img_height / self.imageLabel.height())
            self.main_window.add_point(pos_in_global.x(), pos_in_global.y(), x_real_img, y_real_img)
        else:
            show_marker_manipulation_disabled_warning()

    def add_point(self, x, y, x_img, y_img, new_point_id: int):
        """
        x, y: global coordinates where the marker is to be added
        x_img, y_img: img coordinates where the marker is to be added, considering image's real size
        new_point_id: id for the newly created marker
        """
        # we now have to paint the markers on the img., so we have to translate x, y coords. from global to self.
        new_pos = self.mapFromGlobal(QPoint(x, y))
        new_point = CircleMarker(new_point_id, (x_img, y_img), parent=self)
        new_point.move(new_pos.x() - new_point.marker_size // 2,
                       new_pos.y() - new_point.marker_size // 2)
        new_point.show()
        self.markers[new_point_id] = new_point
        self.update()

    def map_from_self_to_real_image_coordinates(self, coords_in_image_widget: tuple):
        """map to real img. coordinates, taking into account the margin needed so the """
        x = round(coords_in_image_widget[0] * self.img_width / self.imageLabel.width())
        y = round(coords_in_image_widget[1] * self.img_height / self.imageLabel.height())
        margin = round(self.main_window.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE] / 2)
        if x > self.img_width - margin:
            x = self.img_width - margin
        if x < margin:
            x = margin
        if y > self.img_height - margin:
            y = self.img_height - margin
        if y < margin:
            y = margin
        return x, y

    def update_position_from_marker(self, point_id: int, new_x: int, new_y: int):
        """
        point_id: id of the marker whose position will be updated
        new_x, new_y: new marker position expressed in global coordinates.
        """
        # we should translate new_x and new_y to self.imageLabel coords.
        current_marker = self.markers.get(point_id)
        translated_coords = self.mapFromGlobal(QPoint(new_x, new_y))
        # take position so that marker stays centered on mouse pos.
        new_x = translated_coords.x() - current_marker.marker_size // 2
        new_y = translated_coords.y() - current_marker.marker_size // 2
        if self.point_on_image(new_x, new_y):
            current_marker.move(new_x, new_y)
            current_marker.update_position(self.map_from_self_to_real_image_coordinates((
                translated_coords.x() - current_marker.marker_size // 2,
                translated_coords.y() - current_marker.marker_size // 2)))

    def finish_position_update(self, point_id: int):
        x = self.markers[point_id].pos[0]
        y = self.markers[point_id].pos[1]
        self.main_window.update_position_from_image(point_id, x, y)

    def update_position_from_marker_position_update_widget(self, point_id: int, new_x: int, new_y: int):
        """coords are expressed in img coords"""
        current_marker = self.markers.get(point_id)
        x_on_widget = round(new_x * self.imageLabel.width() / self.img_width)
        y_on_widget = round(new_y * self.imageLabel.height() / self.img_height)
        current_marker.move(x_on_widget, y_on_widget)

    def point_on_image(self, x: int, y: int):
        pixmap__width = self.imageLabel.pixmap().width()
        pixmap__height = self.imageLabel.pixmap().height()
        x_img_vs_widget_px_relation = self.img_width / pixmap__width
        y_img_vs_widget_px_relation = self.img_height / pixmap__height
        margin = round(self.main_window.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE] / 2)
        x_margin = margin / x_img_vs_widget_px_relation
        y_margin = margin / y_img_vs_widget_px_relation
        return pixmap__width - x_margin >= x >= x_margin and pixmap__height - y_margin >= y >= y_margin

    def remove_marker(self, marker_id: int):
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
