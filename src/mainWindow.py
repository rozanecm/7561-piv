import os

import PIL.Image
import numpy as np
import piv
import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from piv.model import Point, InputPIV

from src.SettingsBearer import SettingsBearer
from src.constants.constants import Constants
from src.widgets.HistoricData.HistoricData import HistoricDataWidget
from src.widgets.ImageWidget.ImageWidget import ImageWidget
from src.widgets.MarkersManagement.ModifyMarkersPositionWidget import ModifyMarkersPositionWidget
from src.widgets.Table.Table import Table
from src.widgets.TransportWidget.TransportWidget import TransportWidget


class MainWindow(QWidget):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.settings_bearer = SettingsBearer()
        self.middle_layout = QHBoxLayout()
        self.side_layout = QVBoxLayout()
        self.app = app
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.markers = {}
        self.results = []
        self.alg_start_time: int = 0    # time.time() when alg starts running
        self.alg_running = False
        self.get_img_sample = False

        self.image_widget = ImageWidget(self.settings_bearer, parent=self)
        self.marker_position_update_widget = ModifyMarkersPositionWidget(parent=self)
        self.table_widget = Table()
        self.transport_widget = TransportWidget(main_window=self)
        # TODO rename historic data widget
        self.historic_data_widget = HistoricDataWidget()

        self.init_gui()

    def init_gui(self):
        self.init_main_window_properties()
        self.set_main_layout()
        self.set_middle_layout()

        self.show()

    def set_main_layout(self):
        self.layout.addLayout(self.middle_layout)
        self.layout.addWidget(self.historic_data_widget)

    def set_middle_layout(self):
        self.side_layout.addWidget(self.table_widget)
        self.side_layout.addStretch()
        self.side_layout.addWidget(self.transport_widget)
        self.side_layout.addStretch()
        self.side_layout.addWidget(self.marker_position_update_widget)

        self.middle_layout.addWidget(self.image_widget)

        self.middle_layout.addStretch()
        self.middle_layout.addLayout(self.side_layout)

    def init_main_window_properties(self):
        self.setWindowTitle('PIV')
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../res/icon.png"))
        self.setWindowIcon(QtGui.QIcon(icon_path))

    def add_point(self, position_x: int = 0, position_y: int = 0,
                  position_x_real_image: int = 0, position_y_real_image: int = 0):
        """
        position_x: global position for click's x coordinate
        position_y: global position for click's y coordinate
        position_x_real_image: global position for click's x coordinate, considering image's real size coordinates
        position_y_real_image: global position for click's y coordinate, considering image's real size coordinates
        """
        new_point_id = self.get_new_point_id()
        self.image_widget.image.add_point(position_x,
                                          position_y,
                                          position_x_real_image,
                                          position_y_real_image,
                                          new_point_id)
        self.markers[new_point_id] = {"position_x": position_x_real_image,
                                      "position_y": position_y_real_image}
        self.table_widget.add_marker(str(new_point_id), position_x_real_image, position_y_real_image)
        margin = round(self.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE] / 2)
        self.marker_position_update_widget.set_min_max_x_value(margin, self.image_widget.image.img_width - margin)
        self.marker_position_update_widget.set_min_max_y_value(margin, self.image_widget.image.img_height - margin)
        self.marker_position_update_widget.enable_spinboxes()
        self.marker_position_update_widget.add_marker(new_point_id, (position_x_real_image, position_y_real_image))
        self.settings_bearer.update_settings(Constants.SETTINGS_MARKERS, self.markers)
        self.transport_widget.enable_start_button()

    def get_new_point_id(self) -> int:
        return 1 if len(self.markers.keys()) == 0 else max(self.markers.keys()) + 1

    def update_position_from_image(self, marker_id: int, new_x: int, new_y: int):
        """COORDS come in real img coords."""
        self.table_widget.update_marker_position(marker_id, new_x, new_y)
        self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (new_x, new_y))
        self.markers[marker_id] = {"position_x": new_x, "position_y": new_y}
        self.settings_bearer.update_settings(Constants.SETTINGS_MARKERS, self.markers)

    def update_position_from_marker_position_update_widget(self, marker_id: int, new_x: int, new_y: int):
        """coord come in img coords."""
        self.table_widget.update_marker_position(marker_id, new_x, new_y)
        self.image_widget.image.update_position_from_marker_position_update_widget(marker_id, new_x, new_y)
        self.markers[marker_id] = {"position_x": new_x, "position_y": new_y}
        self.settings_bearer.update_settings(Constants.SETTINGS_MARKERS, self.markers)

    def remove_marker(self, marker_id):
        self.table_widget.remove_marker(marker_id)
        self.marker_position_update_widget.remove_marker(marker_id)
        del self.markers[marker_id]
        self.reorder_markers()
        if len(self.markers.keys()) == 0:
            self.marker_position_update_widget.disable_spinboxes()
            self.transport_widget.disable_start_button()
        self.settings_bearer.update_settings(Constants.SETTINGS_MARKERS, self.markers)

    def reorder_markers(self):
        l1 = [x + 1 for x in range(len(self.markers.keys()))]
        l2 = list(self.markers.values())
        self.markers = dict(zip(l1, l2))

    def receive_img_from_img_reader(self, img: PIL.Image.Image) -> None:
        if self.alg_running or self.get_img_sample:
            self.image_widget.image.set_image_from_PIL(img)
            self.get_img_sample = False

    def check_if_markers_margin_is_not_exceeding_imgs_limits(self):
        for marker_id in self.markers:
            margin = round(self.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE] / 2)
            x = self.markers[marker_id]["position_x"]
            y = self.markers[marker_id]["position_y"]
            img_width = self.image_widget.image.img_width
            img_height = self.image_widget.image.img_height
            self.marker_position_update_widget.set_min_max_x_value(margin, img_width - margin)
            self.marker_position_update_widget.set_min_max_y_value(margin, img_height - margin)
            if x > img_width - margin:
                x = img_width - margin
                self.table_widget.update_marker_position(marker_id, x, y)
                self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (x, y))
            if x < margin:
                x = margin
                self.table_widget.update_marker_position(marker_id, x, y)
                self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (x, y))
            if y > img_height - margin:
                y = img_height - margin
                self.table_widget.update_marker_position(marker_id, x, y)
                self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (x, y))
            if y < margin:
                y = margin
                self.table_widget.update_marker_position(marker_id, x, y)
                self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (x, y))
            self.markers[marker_id]["position_x"] = x
            self.markers[marker_id]["position_y"] = y

    def init_chart_data(self):
        """
        This methods makes sure the chart will have the data structures initialized once the results start coming in.
        """
        self.historic_data_widget.init_chart_data(len(self.markers))

    def alg_start(self):
        self.alg_running = True
        self.alg_start_time = time.time()
        self.marker_position_update_widget.disable_spinboxes()

    def alg_stop(self):
        self.results = []
        self.marker_position_update_widget.enable_spinboxes()

    def new_results(self, new_results: dict) -> None:
        """for reference on what exactly the data dict contains, please refer to the piv module."""
        timestamp = time.time() - self.alg_start_time
        for identifier, velocities in new_results.items():
            d = {'timestamp': timestamp,
                 'vel_x': velocities.u,
                 'vel_y': velocities.v,
                 'pos_x': self.markers[identifier]["position_x"],
                 'pos_y': self.markers[identifier]["position_y"]
                 }
            self.results.append(d)
        self.historic_data_widget.update_chart(new_results, timestamp)
        self.table_widget.update_velocities(new_results)

    def send_image_to_backend(self, left_half: PIL.Image.Image, right_half: PIL.Image.Image):
        """
        new_img: whole img, which contains two imgs
        """
        if self.alg_running:
            points = {}
            for marker_id, marker_imgs in self.get_cropped_imgs(left_half.convert("L"),
                                                                right_half.convert("L"),
                                                                self.main_window.markers).items():
                marker = self.main_window.settings_bearer.settings[Constants.SETTINGS_MARKERS][marker_id]
                points[marker_id] = Point(marker['position_x'], marker['position_y'], marker_imgs)
            data = InputPIV(points,
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_DELTA_T],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_PPM],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_ROI])
            piv_results = piv.calculate_piv(data)
            print(piv_results)
            self.main_window.new_results(piv_results)

    def get_cropped_imgs(self, left_half: PIL.Image.Image, right_half: PIL.Image.Image, markers: dict) -> dict:
        """crop imgs of size of ROI, with marker centered in the area"""
        imgs = {}
        roi_value = self.main_window.settings_bearer.settings[Constants.SETTINGS_ROI]
        width, height = roi_value, roi_value
        for key in markers:
            x = markers[key]["position_x"]
            y = markers[key]["position_y"]
            left = x - (width // 2)
            top = y - (height // 2)
            right = left + width
            bottom = top + height
            left_half_crop = left_half.crop((left, top, right, bottom))  # PIL.Image.Image
            right_half_crop = right_half.crop((left, top, right, bottom))  # PIL.Image.Image
            imgs[key] = np.array([np.array(np.asarray(left_half_crop)), np.array(np.asarray(right_half_crop))])
        return imgs
