import os

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel

from src.SettingsBearer import SettingsBearer
from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.ImageWidget.Image import Image
from src.widgets.ImageWidget.ROISelectorWidget import ROISelectorWidget
from src.widgets.ImageWidget.selectionSize import SelectionSizeWidget
from src.widgets.SettingsWidget.SettingsWidget import SettingsWidget
from src.widgets.StatusBar.StatusBar import StatusBar


def get_vector_reference_image_widget():
    layout = QHBoxLayout()
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../res/terna referencia.png"))
    image_label = QLabel()
    image_label.setPixmap(QPixmap(path))

    layout.addStretch()
    layout.addWidget(image_label)
    layout.addStretch()
    return layout


class ImageWidget(GroupBox):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    def __init__(self, settings_bearer: SettingsBearer, parent=None):
        # parent: main window
        super().__init__("Imagen", parent=parent)

        self.settings_layout = QVBoxLayout()
        self.settings_bearer = settings_bearer
        self.layout = QVBoxLayout()
        self.main_layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.image = Image(self.settings_bearer, self.parent(), parent=self)

        self.settings_widget = SettingsWidget(self.settings_bearer, main_window=self.parent())
        self.roi_selector_widget = ROISelectorWidget(self.settings_bearer, main_window=self.parent())
        self.selection_size_widget = SelectionSizeWidget(self.settings_bearer, main_window=self.parent(), parent=self)
        self.vector_reference_image = get_vector_reference_image_widget()

        self.status_bar = StatusBar()

        self.setup_gui()

        self.show()

    def setup_gui(self):
        self.main_layout.addWidget(self.image)
        self.settings_layout.addStretch()
        self.settings_layout.addWidget(self.settings_widget)
        self.settings_layout.addWidget(self.selection_size_widget)
        self.settings_layout.addWidget(self.roi_selector_widget)
        self.settings_layout.addLayout(self.vector_reference_image)
        self.settings_layout.addStretch()
        self.main_layout.addLayout(self.settings_layout)
        self.layout.addWidget(self.status_bar)
        self.layout.addLayout(self.main_layout)
