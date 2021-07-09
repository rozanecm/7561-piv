import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.MarkersManagement.ModifyMarkersPositionWidget import ModifyMarkersPositionWidget


class MarkersManagementWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración de puntos", parent=parent)
        self.quitar_punto_button = QtWidgets.QPushButton("Quitar punto")
        self.agregar_punto_button = QtWidgets.QPushButton("Agregar punto")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(15)

        self.parent = parent

        self.setMinimumHeight(75)

        self.set_gui()

    def set_gui(self):
        self.set_markers_management_buttons()
        self.layout.addWidget(ModifyMarkersPositionWidget())

    def set_markers_management_buttons(self):
        buttons_layout = QHBoxLayout()

        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/add_marker.png"))
        self.agregar_punto_button.setIcon(QIcon(icon_path))
        self.agregar_punto_button.clicked.connect(self.agregar_punto_button_clicked)

        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/remove_marker.png"))
        self.quitar_punto_button.setIcon(QIcon(icon_path))
        self.quitar_punto_button.setEnabled(False)
        self.quitar_punto_button.clicked.connect(self.quitar_punto_button_clicked)

        buttons_layout.addWidget(self.agregar_punto_button)
        buttons_layout.addWidget(self.quitar_punto_button)

        self.layout.addLayout(buttons_layout)

    def agregar_punto_button_clicked(self):
        self.parent.add_point()

    def quitar_punto_button_clicked(self):
        pass
