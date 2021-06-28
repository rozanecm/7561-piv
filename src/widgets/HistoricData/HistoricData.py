from PyQt5.QtChart import QLineSeries, QChart, QChartView
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class HistoricDataWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QVBoxLayout()

        line_series = QLineSeries()
        line_series.append(QPoint(0, 4))
        chart = QChart()
        chart.addSeries(line_series)
        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(view)

        self.button = QPushButton("Obtener CSV")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(lambda: self.process_csv_click())
