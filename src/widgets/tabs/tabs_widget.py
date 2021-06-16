from PyQt5.QtWidgets import QWidget

from widgets.tabs.tabs import Ui_Form


class tabWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)