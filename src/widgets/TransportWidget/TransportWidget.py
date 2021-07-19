import os
from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox


class TransportWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Control", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.set_gui()

    def set_gui(self):
        play_button = self.make_button("Iniciar", os.path.join(os.path.dirname(__file__), "../../../res/play_icon.png"), self.process_play_button_click)
        stop_button = self.make_button("Detener", os.path.join(os.path.dirname(__file__), "../../../res/pause_icon.png"), self.process_stop_button_click)
        get_preview_button = self.make_button("Obtener previsualizacion", os.path.join(os.path.dirname(__file__), "../../../res/get_preview_icon.png"), self.process_get_preview_button_click)
        self.layout.addWidget(get_preview_button)
        play_stop_layout = QHBoxLayout()
        self.layout.addLayout(play_stop_layout)
        play_stop_layout.addWidget(play_button)
        play_stop_layout.addWidget(stop_button)

    @staticmethod
    def make_button(label: str, path: str, func: Callable) -> QPushButton:
        new_button = QPushButton(label)
        icon_path = os.path.abspath(path)
        new_button.setIcon(QIcon(icon_path))
        new_button.clicked.connect(lambda: func())
        return new_button

    def process_play_button_click(self):
        print("play button pressed")

    def process_stop_button_click(self):
        print("stop button pressed")

    def process_get_preview_button_click(self):
        print("get_preview_button pressed")
