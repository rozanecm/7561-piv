import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.MarkersManagement.ModifyMarkersPositionWidget import ModifyMarkersPositionWidget


class MarkersManagementWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración de puntos", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setMinimumHeight(75)

        self.set_gui()

    def set_gui(self):
        self.set_markers_management_buttons()
        self.layout.addWidget(ModifyMarkersPositionWidget())

    def set_markers_management_buttons(self):
        buttons_layout = QHBoxLayout()

        agregar_punto_button = QtWidgets.QPushButton("Agregar punto")
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/add_marker.png"))
        agregar_punto_button.setIcon(QIcon(icon_path))

        quitar_punto_button = QtWidgets.QPushButton("Quitar punto")
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/remove_marker.png"))
        quitar_punto_button.setIcon(QIcon(icon_path))

        buttons_layout.addWidget(agregar_punto_button)
        buttons_layout.addWidget(quitar_punto_button)

        self.layout.addLayout(buttons_layout)
