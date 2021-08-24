import os
import time
import numpy as np
from typing import Dict

from PyQt5.QtChart import QChart, QChartView, QValueAxis, QLineSeries
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.HistoricData.ChartRefreshRateSettings import ChartRefreshRateSetting
from src.widgets.HistoricData.ChartScaleSettings import ChartScaleSettingsWidget
from src.widgets.HistoricData.Modal import Modal
from src.widgets.HistoricData.VelocitySelection import VelocitySelectionWidget
from src.widgets.HistoricData.typedef import line


class HistoricDataWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Valores históricos", parent=parent)
        self.num_of_points_to_represent = Constants.CHART_SECONDS_REPRESENTED * Constants.IMAGE_INPUT_FRECUENCY_IN_HZ
        self.data = {}
        self.layout = QHBoxLayout()

        self.chart = QChart()
        self.view = QChartView(self.chart)

        self.chart_scale_settings = ChartScaleSettingsWidget(parent=self)
        self.velocity_selection = VelocitySelectionWidget()
        self.side_layout = QVBoxLayout()
        self.settings_button = QPushButton("Configuración")
        self.setup_settings_button()
        self.refresh_rate_setting = ChartRefreshRateSetting()

        self.line_series: Dict[int, line] = {}
        self.last_chart_refresh_timestamp_ms = 0

        self.axis_x = QValueAxis()
        self.axis_y = QValueAxis()
        self.setup_axes()
        self.setup_chart()

        self.setup_general_layout()

    def setup_settings_button(self):
        self.settings_button.clicked.connect(lambda: self.process_settings_click())
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/settings.png"))
        self.settings_button.setIcon(QIcon(icon_path))

    def setup_general_layout(self):
        self.layout.addWidget(self.view)
        self.side_layout.addStretch()
        self.side_layout.addWidget(self.velocity_selection)
        self.side_layout.addWidget(self.chart_scale_settings)
        self.side_layout.addWidget(self.settings_button)
        self.side_layout.addWidget(self.refresh_rate_setting)
        self.side_layout.addStretch()
        self.layout.addLayout(self.side_layout)
        self.setLayout(self.layout)

    def setup_axes(self):
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("t(s)")
        self.axis_y.setTitleText("v(mm/s)")
        self.axis_y.setLabelFormat("%i")

    def setup_chart(self):
        self.chart.setTitle("Evolución")
        self.chart.setTheme(QChart.ChartThemeBlueIcy)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

    def init_chart_data(self, num_of_markers: int) -> None:
        self.data.clear()
        self.clear_chart()
        self.line_series: Dict[int, line] = {}
        self.chart.removeAllSeries()
        for i in range(num_of_markers):
            self.data[i + 1] = {}
            self.data[i + 1]['vel_x'] = []
            self.data[i + 1]['vel_y'] = []
            self.data[i + 1]['vel_magnitude'] = []

            self.line_series[i + 1] = {'is_visible': True, 'series': QLineSeries()}
            self.line_series[i + 1]['series'].setName(str(i + 1))
            self.chart.addSeries(self.line_series[i + 1]['series'])
            self.line_series[i + 1]['series'].attachAxis(self.axis_y)
            self.line_series[i + 1]['series'].attachAxis(self.axis_x)
        self.axis_y.setMin(self.chart_scale_settings.min_y_spinbox.value())
        self.axis_y.setMax(self.chart_scale_settings.max_y_spinbox.value())

    def set_y_max_value(self, max_value: int):
        self.axis_y.setMax(max_value)

    def set_y_min_value(self, min_value: int):
        self.axis_y.setMin(min_value)

    def process_settings_click(self):
        modal = Modal(self.line_series, self)
        modal.exec()

    def enable_line_toggle(self, line_id: int, new_value: bool):
        self.line_series[line_id]['is_visible'] = new_value
        self.line_series[line_id]['series'].show() if new_value else self.line_series[line_id]['series'].hide()

    def update_chart(self, data: dict, timestamp: float) -> None:
        """for reference on what exactly the data dict contains, please refer to the piv module."""
        for identifier, velocities in data.items():
            self.data[identifier]['vel_x'].append((timestamp, velocities.u))
            self.data[identifier]['vel_y'].append((timestamp, velocities.v))
            self.data[identifier]['vel_magnitude'].append((timestamp, np.linalg.norm([velocities.u, velocities.v])))

        timestamp_in_ms = time.time_ns() * 1e-6
        if self.last_chart_refresh_timestamp_ms + (1 / Constants.CHART_REFRESH_RATE_IN_HZ) * 1e3 < timestamp_in_ms:
            self.refresh_chart_visually(timestamp)
            self.last_chart_refresh_timestamp_ms = timestamp_in_ms

    def get_velocity_to_show_key(self) -> str:
        current_option = self.velocity_selection.combo_box.currentText()
        if current_option == Constants.VELOCITY_MAGNITUDE:
            return 'vel_magnitude'
        if current_option == Constants.VELOCITY_VECT_X:
            return 'vel_x'
        if current_option == Constants.VELOCITY_VECT_Y:
            return 'vel_y'
        return 'vel_magnitude'

    def refresh_chart_visually(self, last_timestamp: float):
        for identifier in self.data.keys():
            self.line_series[identifier]['series'].clear()
            points = []
            vel_to_show = self.get_velocity_to_show_key()
            for e in self.data[identifier][vel_to_show]:
                if e[0] > (last_timestamp - Constants.CHART_SECONDS_REPRESENTED):
                    points.append(QPointF(e[0], e[1]))
            self.line_series[identifier]['series'].append(points)
        self.axis_x.setMax(last_timestamp)
        self.axis_x.setMin(max(0, last_timestamp - Constants.CHART_SECONDS_REPRESENTED))

    def clear_chart(self):
        for identifier in self.data.keys():
            self.line_series[identifier]['series'].clear()
