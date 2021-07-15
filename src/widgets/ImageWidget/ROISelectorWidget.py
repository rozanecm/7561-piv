from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpinBox

from src.constants.constants import Constants
from src.widgets.GroupBox.GroupBox import GroupBox


class ROISelectorWidget(GroupBox):
    def __init__(self, outputter, parent=None):
        super().__init__("ROI", parent=parent)
        self.outputter = outputter
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.roi_input = QSpinBox()
        self.roi_input.valueChanged.connect(lambda: self.roi_update())

        self.set_gui()

    def set_gui(self):
        self.layout.addWidget(self.roi_input)

    def roi_update(self):
        self.outputter.transmit_message(Constants.MSG_TYPE_ROI_UPDATE, self.roi_input.value())
