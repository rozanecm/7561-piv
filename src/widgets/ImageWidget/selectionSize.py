from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QButtonGroup

from src.widgets.GroupBox.GroupBox import GroupBox


class SelectionSizeWidget(GroupBox):
    def __init__(self, parent=None):
        super().__init__("Tamaño de selección", parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_group = QButtonGroup()

        self.init_gui()
        self.setMinimumWidth(200)

    def init_gui(self):
        radio_button_8x8 = QRadioButton("8x8")
        radio_button_16x16 = QRadioButton("16x16")
        radio_button_32x32 = QRadioButton("32x32")
        radio_button_other = QRadioButton("otro")
        self.layout.addWidget(radio_button_8x8)
        self.layout.addWidget(radio_button_16x16)
        self.layout.addWidget(radio_button_32x32)
        self.layout.addWidget(radio_button_other)

        radio_button_8x8.setChecked(True)

        self.button_group.addButton(radio_button_8x8)
        self.button_group.addButton(radio_button_16x16)
        self.button_group.addButton(radio_button_32x32)
        self.button_group.addButton(radio_button_other)
        self.button_group.buttonClicked.connect(lambda button: self.button_pressed(button))


    def button_pressed(self, button: QRadioButton):
        print(button.text())
