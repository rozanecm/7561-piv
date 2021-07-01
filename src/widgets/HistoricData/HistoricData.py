from PyQt5.QtChart import QLineSeries, QChart, QChartView, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import QPoint, Qt, QPointF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout


class HistoricDataWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()

        line_series = QLineSeries()
        line_series.append([QPointF(0, 6),
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
        chart.setAnimationOptions(QChart.AllAnimations)

        axis_x = QValueAxis()
        axis_x.setRange(0, 30000)
        axis_x.setLabelFormat("%i")
        axis_x.setTitleText("Tiempo (ms)")
        axis_x.setTickCount(13)
        axis_x.setReverse()
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QValueAxis()
        axis_y.setTitleText("Vel. (m/s)")
        axis_y.setLabelFormat("%i")
        chart.addAxis(axis_y, Qt.AlignLeft)

        chart.addSeries(line_series)
        line_series.attachAxis(axis_y)
        line_series.attachAxis(axis_x)

        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(view)

        self.button = QPushButton("Obtener CSV")
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(lambda: self.process_csv_click())

    def process_csv_click(self):
        print("Clicked csv button heheeyy")
