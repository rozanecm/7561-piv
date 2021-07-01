from time import sleep

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from random import gauss
import threading


class HistoricDataWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()

        self.line_series = QLineSeries()
        self.line_series.append([QPointF(0, 6),
                                 QPointF(1000, 4),
                                 QPointF(2000, 10),
                                 QPointF(3000, 8),
                                 QPointF(4000, 5),
                                 QPointF(5000, 1),
                                 QPointF(6000, 2),
                                 QPointF(7000, 3),
                                 QPointF(8000, 4),
                                 QPointF(9000, 7),
                                 QPointF(10000, 5),
                                 QPointF(11000, 6),
                                 QPointF(25000, 15),
                                 ])

        chart = QChart()
        chart.setTitle("Evolución histórica (últimos 30 seg)")
        chart.setTheme(QChart.ChartThemeBlueIcy)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QValueAxis()
        axis_x.setRange(0, 30000)
        axis_x.setLabelFormat("%i")
        axis_x.setTitleText("Tiempo (ms)")
        axis_x.setTickCount(13)
        axis_x.setReverse()
        chart.addAxis(axis_x, Qt.AlignBottom)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Vel. (m/s)")
        self.axis_y.setLabelFormat("%i")
        chart.addAxis(self.axis_y, Qt.AlignLeft)

        chart.addSeries(self.line_series)
        self.line_series.attachAxis(self.axis_y)
        self.line_series.attachAxis(axis_x)

        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(view)

        self.button = QPushButton("Obtener CSV")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(lambda: self.process_csv_click())

    def process_csv_click(self):
        for i in range(1000):
            threading.Timer(i*0.5, self.update_chart).start()

    def update_chart(self):
        self.line_series.clear()
        points = []
        for i in range(30):
            points.append(QPointF(i * 1000, gauss(10, 2)))
        self.line_series.append(points)
        new_min, new_max = self.get_min_max_points()
        self.axis_y.setRange(new_min, new_max)

    def get_min_max_points(self):
        max_y_value_in_chary = -9e25
        min_y_value_in_chary = 9e25
        for point in self.line_series.pointsVector():
            if point.y() < min_y_value_in_chary:
                min_y_value_in_chary = point.y()
            if point.y() > max_y_value_in_chary:
                max_y_value_in_chary = point.y()

        return min_y_value_in_chary, max_y_value_in_chary
