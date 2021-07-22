from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from src.SettingsBearer import SettingsBearer
from src.widgets.GroupBox.GroupBox import GroupBox
from src.widgets.ImageWidget.Image import Image
from src.widgets.ImageWidget.ROISelectorWidget import ROISelectorWidget
from src.widgets.ImageWidget.selectionSize import SelectionSizeWidget
from src.widgets.SettingsWidget.SettingsWidget import SettingsWidget
from src.widgets.StatusBar.StatusBar import StatusBar


class ImageWidget(GroupBox):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    def __init__(self, settings_bearer: SettingsBearer, parent=None):
        super().__init__("Imagen", parent=parent)

        self.settings_bearer = settings_bearer
        self.layout = QVBoxLayout()
        self.main_layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.image = Image(self.settings_bearer, self.parent())

        self.main_layout.addWidget(self.image)
        self.settings_layout = QVBoxLayout()
        self.settings_layout.addStretch()
        self.settings_layout.addWidget(SettingsWidget(self.settings_bearer))
        self.settings_layout.addWidget(SelectionSizeWidget(self.settings_bearer))
        self.settings_layout.addWidget(ROISelectorWidget(self.settings_bearer))
        self.settings_layout.addStretch()
        self.main_layout.addLayout(self.settings_layout)

        self.status_bar = StatusBar()
        self.layout.addWidget(self.status_bar)
        self.layout.addLayout(self.main_layout)

        self.show()
