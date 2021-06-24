import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from src.widgets.tabs.tabs import Ui_Form


class TabWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.parent = parent
        self.add_icons_to_buttons()

    def addPoint(self):
        self.parent.add_point()

    def add_icons_to_buttons(self):
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/remove_marker.png"))
        self.quitar_punto_button.setIcon(QIcon(icon_path))

        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/add_marker.png"))
        self.agregar_punto_button.setIcon(QIcon(icon_path))

        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/reset.png"))
        self.restablecer_button.setIcon(QIcon(icon_path))
