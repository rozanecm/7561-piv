import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.MarkersManagement.ModifyMarkersPositionWidget import ModifyMarkersPositionWidget


class MarkersManagementWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Configuración de puntos", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(15)

        self.parent = parent

        self.setMinimumHeight(75)

        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(ModifyMarkersPositionWidget())
