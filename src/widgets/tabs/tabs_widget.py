from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

from src.widgets.tabs.tabs import Ui_Form


class TabWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.parent = parent

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print(a0.pos())

    def addPoint(self):
        self.parent.add_point()
