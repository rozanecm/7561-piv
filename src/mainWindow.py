import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

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
        self.outputter = SettingsBearer()
        self.middle_layout = QHBoxLayout()
        self.side_layout = QVBoxLayout()
        self.app = app
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.points = {}
        self.accept_imgs = False
        self.get_img_sample = False

        self.image_widget = ImageWidget(self.outputter, parent=self)
        self.marker_position_update_widget = ModifyMarkersPositionWidget(parent=self)
        self.table_widget = Table()
        self.transport_widget = TransportWidget(main_window=self)
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
        self.points[new_point_id] = {"position_x": position_x_real_image,
                                     "position_y": position_y_real_image}
        self.table_widget.add_marker(str(new_point_id), position_x_real_image, position_y_real_image)
        self.historic_data_widget.add_line(new_point_id)
        self.marker_position_update_widget.enable_spinboxes()
        self.marker_position_update_widget.add_marker(new_point_id, (position_x_real_image, position_y_real_image))
        self.outputter.update_settings(Constants.SETTINGS_MARKERS, self.points)

    def get_new_point_id(self) -> int:
        return 1 if len(self.points.keys()) == 0 else max(self.points.keys()) + 1

    def update_position_from_image(self, marker_id: int, new_x: int, new_y: int):
        """COORDS come in real img coords."""
        self.table_widget.update_marker_position(marker_id, new_x, new_y)
        self.marker_position_update_widget.update_marker_position_from_main_window(marker_id, (new_x, new_y))
        self.points[marker_id] = {"position_x": new_x, "position_y": new_y}
        self.outputter.update_settings(Constants.SETTINGS_MARKERS, self.points)

    def update_position_from_marker_position_update_widget(self, marker_id: int, new_x: int, new_y: int):
        """coord come in img coords."""
        self.table_widget.update_marker_position(marker_id, new_x, new_y)
        self.image_widget.image.update_position_from_marker_position_update_widget(marker_id, new_x, new_y)
        self.points[marker_id] = {"position_x": new_x, "position_y": new_y}
        self.outputter.update_settings(Constants.SETTINGS_MARKERS, self.points)

    def remove_marker(self, marker_id):
        self.historic_data_widget.remove_line(marker_id)
        self.table_widget.remove_marker(marker_id)
        self.marker_position_update_widget.remove_marker(marker_id)
        del self.points[marker_id]
        self.reorder_markers()
        if len(self.points.keys()) == 0:
            self.marker_position_update_widget.disable_spinboxes()
        self.outputter.update_settings(Constants.SETTINGS_MARKERS, self.points)

    def reorder_markers(self):
        l1 = [x + 1 for x in range(len(self.points.keys()))]
        l2 = list(self.points.values())
        self.points = dict(zip(l1, l2))

    def receive_img_from_img_reader(self, img):
        if self.accept_imgs or self.get_img_sample:
            self.image_widget.image.set_image_from_PIL(img)
            self.get_img_sample = False
