from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from src.widgets.GroupBox.GroupBox import GroupBox


class TransportWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Transporte", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.set_gui()

    def set_gui(self):
        play_button = self.make_play_button()
        stop_button = self.make_stop_button()
        get_preview_button = self.make_get_preview_button()
        self.layout.addWidget(play_button)
        self.layout.addWidget(stop_button)
        self.layout.addWidget(get_preview_button)

    def make_get_preview_button(self):
        get_preview_button = QPushButton("Obtener previsualizacion")
        get_preview_button.clicked.connect(lambda: self.process_get_preview_button_click())
        return get_preview_button

    def make_stop_button(self):
        stop_button = QPushButton("Detener")
        stop_button.clicked.connect(lambda: self.process_stop_button_click())
        return stop_button

    def make_play_button(self):
        play_button = QPushButton("Iniciar")
        play_button.clicked.connect(lambda: self.process_play_button_click())
        return play_button

    def process_play_button_click(self):
        print("play button pressed")

    def process_stop_button_click(self):
        print("stop button pressed")

    def process_get_preview_button_click(self):
        print("get_preview_button pressed")
