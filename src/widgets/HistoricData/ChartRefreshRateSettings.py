from PyQt5.QtWidgets import QSpinBox, QVBoxLayout, QLabel, QHBoxLayout

from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class ChartRefreshRateSetting(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Visualización", parent=parent)
        chart_refresh_rate = self.get_custom_spinbox(lambda value: self.chart_refresh_rate_update(value),
                                                     "Tasa de actualización",
                                                     "Hz",
                                                     Constants.CHART_REFRESH_RATE_IN_HZ)
        chart_seconds_represented = self.get_custom_spinbox(lambda value: self.chart_seconds_represented_update(value),
                                                            "Tiempo a mostrar",
                                                            "s",
                                                            Constants.CHART_SECONDS_REPRESENTED)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addLayout(chart_refresh_rate)
        self.layout.addLayout(chart_seconds_represented)

    @staticmethod
    def get_custom_spinbox(func, label_text: str = "", suffix: str = "", default_value: int = 0) -> QHBoxLayout:
        lay = QHBoxLayout()
        label = QLabel(label_text)
        spinbox = QSpinBox()
        spinbox.setValue(default_value)
        spinbox.setSuffix(suffix)
        spinbox.valueChanged.connect(func)
        lay.addWidget(label)
        lay.addWidget(spinbox)
        return lay

    @staticmethod
    def chart_refresh_rate_update(value):
        Constants.CHART_REFRESH_RATE_IN_HZ = value

    @staticmethod
    def chart_seconds_represented_update(value):
        Constants.CHART_SECONDS_REPRESENTED = value
