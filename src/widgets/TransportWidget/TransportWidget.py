import os
from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox


class TransportWidget(GroupBox):
    def __init__(self, main_window, parent=None):
        super().__init__("Control", parent=parent)
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.set_gui()

    def set_gui(self):
        play_stop_layout = QHBoxLayout()
        self.layout.addLayout(play_stop_layout)
        self.layout.addWidget(self.make_button("Obtener previsualizacion",
                                               os.path.join(os.path.dirname(__file__),
                                                            "../../../res/get_preview_icon.png"),
                                               self.process_get_preview_button_click))
        play_stop_layout.addWidget(self.make_button("Iniciar",
                                                    os.path.join(os.path.dirname(__file__),
                                                                 "../../../res/play_icon.png"),
                                                    self.process_play_button_click))
        play_stop_layout.addWidget(self.make_button("Detener",
                                                    os.path.join(os.path.dirname(__file__),
                                                                 "../../../res/pause_icon.png"),
                                                    self.process_stop_button_click))

    @staticmethod
    def make_button(label: str, path: str, func: Callable) -> QPushButton:
        new_button = QPushButton(label)
        icon_path = os.path.abspath(path)
        new_button.setIcon(QIcon(icon_path))
        new_button.clicked.connect(lambda: func())
        return new_button

    def process_play_button_click(self):
        self.main_window.accept_imgs = True

    def process_stop_button_click(self):
        self.main_window.accept_imgs = False

    def process_get_preview_button_click(self):
        self.main_window.get_img_sample = True
        self.main_window.image_widget.image.can_manipulate_markers = True
