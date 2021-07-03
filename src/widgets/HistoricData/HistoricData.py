from random import gauss
from typing import Dict

from PyQt5 import QtGui
from typing_extensions import TypedDict

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QSplineSeries
from PyQt5.QtCore import Qt, QPointF, QObject, QEvent
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.HistoricData.Modal import Modal


class HistoricDataWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Historic data", parent=parent)
        self.layout = QHBoxLayout()
        line = TypedDict('line', {'is_visible': bool, 'series': QSplineSeries})
        self.line_series: Dict[int, line] = {}

        self.chart = QChart()
        self.chart.setTitle("Evolución histórica (últimos 30 seg)")
        self.chart.setTheme(QChart.ChartThemeBlueIcy)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%i")
        self.axis_x.setTitleText("Tiempo (ms)")
        self.axis_x.setTickCount(13)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Vel. (m/s)")
        self.axis_y.setLabelFormat("%i")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.view)

        self.button = QPushButton("Obtener CSV")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(lambda: self.process_csv_click())

    def add_line(self, marker_id: int):
        self.line_series[marker_id] = {'is_visible': True, 'series': QSplineSeries()}
        self.line_series[marker_id]['series'].setName(str(marker_id))
        self.update_chart(marker_id)
        self.chart.addSeries(self.line_series[marker_id]['series'])
        self.line_series[marker_id]['series'].attachAxis(self.axis_y)
        self.line_series[marker_id]['series'].attachAxis(self.axis_x)

    def set_y_range(self, min_value: int, max_value: int):
        self.axis_x.setRange(min_value, max_value)

    def process_csv_click(self):
        modal = Modal(list(self.line_series.keys()))
        modal.exec()

    def update_chart(self, line_id: int):
        self.line_series[line_id]['series'].clear()
        points = []
        for i in range(30):
            points.append(QPointF(i * 1000, gauss(10, 2)))
        self.line_series[line_id]['series'].append(points)
        new_min, new_max = self.get_min_max_points(line_id)
        self.axis_y.setRange(new_min, new_max)

    def get_min_max_points(self, line_id: int):
        max_y_value_in_chary = -9e25
        min_y_value_in_chary = 9e25
        for point in self.line_series[line_id]['series'].pointsVector():
            if point.y() < min_y_value_in_chary:
                min_y_value_in_chary = point.y()
            if point.y() > max_y_value_in_chary:
                max_y_value_in_chary = point.y()

        return min_y_value_in_chary, max_y_value_in_chary
