from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

from src.widgets.tabs.tabs import Ui_Form


class TabWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.remove_initial_tabs()
        self.parent = parent

    def remove_initial_tabs(self):
        self.tabWidget.removeTab(0)
        self.tabWidget.removeTab(0)

    def add_point(self):
        self.tabWidget.addTab()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(a0.pos())

    def addPoint(self):
        self.parent.add_point()

    def update_position_x(self, new_x: int, point_id: int):
        print("updating pos x for point {} from tabs widget to: {}".format(point_id, new_x))
