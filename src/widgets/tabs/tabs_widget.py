from PyQt5.QtWidgets import QWidget

from src.widgets.tabs.tabs import Ui_Form


class TabWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.tabWidget.removeTab(1)

    def add_point(self):
        self.tabWidget.addTab()
