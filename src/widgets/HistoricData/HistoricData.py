import os
from random import gauss
from typing import Dict

from PyQt5.QtChart import QChart, QChartView, QValueAxis, QSplineSeries
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.HistoricData.ChartScaleSettings import ChartScaleSettingsWidget
from src.widgets.HistoricData.Modal import Modal
from src.widgets.HistoricData.VelocitySelection import VelocitySelectionWidget
from src.widgets.HistoricData.typedef import line


class HistoricDataWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Historic data", parent=parent)
        self.layout = QHBoxLayout()

        self.chart = QChart()
        self.view = QChartView(self.chart)

        self.chart_scale_settings = ChartScaleSettingsWidget(parent=self)
        self.velocity_selection = VelocitySelectionWidget()
        self.side_layout = QVBoxLayout()
        self.settings_button = QPushButton("Configuración")
        self.setup_settings_button()
        self.download_csv_button = QPushButton("Obtener CSV")
        self.setup_download_button()

        self.line_series: Dict[int, line] = {}

        self.axis_x = QValueAxis()
        self.axis_y = QValueAxis()
        self.setup_axes()
        self.setup_chart()

        self.setup_general_layout()

    def setup_download_button(self):
        self.download_csv_button.clicked.connect(lambda: self.process_csv_click())
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/save.png"))
        self.download_csv_button.setIcon(QIcon(icon_path))

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
        self.side_layout.addWidget(self.download_csv_button)
        self.side_layout.addStretch()
        self.layout.addLayout(self.side_layout)
        self.setLayout(self.layout)

    def setup_axes(self):
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("Tiempo (ms)")
        self.axis_x.setTickCount(13)
        self.axis_y.setTitleText("Vel. (m/s)")
        self.axis_y.setLabelFormat("%i")

    def setup_chart(self):
        self.chart.setTitle("Evolución histórica (últimos 30 seg)")
        self.chart.setTheme(QChart.ChartThemeBlueIcy)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

    def add_line(self, marker_id: int):
        self.line_series[marker_id] = {'is_visible': True, 'series': QSplineSeries()}
        self.line_series[marker_id]['series'].setName(str(marker_id))
        self.update_chart(marker_id)
        self.chart.addSeries(self.line_series[marker_id]['series'])
        self.line_series[marker_id]['series'].attachAxis(self.axis_y)
        self.line_series[marker_id]['series'].attachAxis(self.axis_x)

    def remove_line(self, marker_id: int):
        print(self.line_series)
        self.chart.removeSeries(self.line_series[marker_id]['series'])
        del self.line_series[marker_id]
        self.reorder_line_series()
        print(self.line_series)

        for current_marker_id, serie in zip(self.line_series.keys(), self.line_series.values()):
            print("adding serie: {}, id: {}".format(serie, current_marker_id))
            serie['series'].setName(str(current_marker_id))

    def reorder_line_series(self):
        l1 = [x + 1 for x in range(len(self.line_series.keys()))]
        l2 = list(self.line_series.values())
        self.line_series = dict(zip(l1, l2))

    def set_y_range(self, min_value: int, max_value: int):
        self.axis_x.setRange(min_value, max_value)

    def set_y_max_value(self, max_value: int):
        self.axis_y.setMax(max_value)

    def set_y_min_value(self, min_value: int):
        self.axis_y.setMin(min_value)

    def process_csv_click(self):
        print("clicked csv click")

    def process_settings_click(self):
        modal = Modal(self.line_series, self)
        modal.exec()

    def enable_line_toggle(self, line_id: int, new_value: bool):
        self.line_series[line_id]['is_visible'] = new_value
        self.line_series[line_id]['series'].show() if new_value else self.line_series[line_id]['series'].hide()

    def update_chart(self, line_id: int):
        self.line_series[line_id]['series'].clear()
        points = []
        for i in range(30):
            points.append(QPointF(i * 1000, gauss(10, 2)))
        self.line_series[line_id]['series'].append(points)

    def change_velocity_type(self, velocity_type: str):
        print("chart should now be showing", velocity_type)
