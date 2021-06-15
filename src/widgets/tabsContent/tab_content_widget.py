from PyQt5.QtWidgets import QWidget

from widgets.tabsContent.tab_content import Ui_TabContent


class TabContent(QWidget, Ui_TabContent):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
