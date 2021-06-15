import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, \
    QButtonGroup, QCheckBox, QGridLayout, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter

from components.tabs.tabs import Ui_Form


class myClassForTabs(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)


# sample empty widget
# src: https://www.geeksforgeeks.org/creating-custom-widgets-in-pyqt5/
# class MyWidget(QtWidgets.QWidget):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.layout = QtWidgets.QGridLayout()
# 		self.setLayout(self.layout)

class EchoText(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.textbox = QLineEdit()
        self.echo_label = QLabel('')

        self.textbox.textChanged.connect(self.textbox_text_changed)

        self.layout.addWidget(self.textbox, 0, 0)
        self.layout.addWidget(self.echo_label, 1, 0)

    def textbox_text_changed(self):
        self.echo_label.setText(self.textbox.text())


class SizeSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QWidget.__init__(self, parent=parent)
        self.b_group = QButtonGroup()  # Create instance of QButtonGroup
        # Create two checkboxes
        cb_1 = QCheckBox("CB 1")
        cb_2 = QCheckBox("CB 2")
        # Add checkboxes into QButtonGroup
        self.b_group.addButton(cb_1)
        self.b_group.addButton(cb_2)
        # Connect all buttons in a group to one signal
        self.b_group.buttonClicked.connect(self.cbClicked)

    def cbClicked(self, cb):
        print(cb)


class ImageWidget(QWidget):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    #
    def __init__(self, parent=None):
        # QWidget.__init__(self, parent=parent)
        super().__init__(parent=parent)
        self.pixmap = QPixmap("../res/icon.png")
        path = "../res/icon.png"

        self.image = QLabel()
        self.image.setPixmap(QPixmap(path))
        self.image.setText("lkajsdlkfjasdf")
        # self.image.pixmap().scaled(532)
        self.image.setObjectName("image")
        self.image.mousePressEvent = self.getPos
        # self.image.setMouseTracking(True)
        print("widget size:", self.frameSize())
        print("widget size:", self.size())
        print("widget size:", self.geometry())

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print("hehe")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}; current size: {}".format(x, y, self.size()))
        print("widget size:", self.frameSize())


    def getPos(self, event):
        print("vnm")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}".format(x,y))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.set_size()
        self.setWindowTitle('PIV')
        self.setWindowIcon(QtGui.QIcon('../res/icon.png'))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # self.layout.addWidget(EchoText())
        self.layout.addWidget(ImageWidget())
        self.layout.addWidget(myClassForTabs())

        # self.b_group = QButtonGroup()  # Create instance of QButtonGroup
        # cb_1 = QCheckBox("CB 1")
        # cb_2 = QCheckBox("CB 2")
        # # Add checkboxes into QButtonGroup
        # self.b_group.addButton(cb_1)
        # self.b_group.addButton(cb_2)
        # # Connect all buttons in a group to one signal
        # self.b_group.buttonClicked.connect(self.cbClicked)
        #
        # # box layout docs: https://doc.qt.io/qt-5/qboxlayout.html
        # # vbox = QVBoxLayout()
        # # # vbox.addWidget(QPushButton("b1"))
        # # vbox.addWidget(SizeSelector())
        # # # vbox.addStretch()
        # #
        # # hbox = QHBoxLayout()
        # # # hbox.addStrut(500)
        # # # hbox.addWidget(ImageWidget(), 5)
        # # hbox.addWidget(QPushButton("b2"), 2)
        # #
        # # vbox.addLayout(hbox)
        # #
        # # self.setLayout(vbox)
        self.show()



    def cbClicked(self, cb):
        print(cb)

    def set_size(self):
        minimum_size = self.get_minimum_size()
        self.setMinimumSize(minimum_size[0], minimum_size[1])

    @staticmethod
    def get_minimum_size(width_fraction=0.9, height_fraction=0.8):
        """
        :return min_width, min_height of the window.
        :argument width_fraction: the amount of the available width the actual screen will take
        :argument height_fraction: the amount of the available height the actual screen will take
        """
        screen = app.primaryScreen()

        # for more screen properties available: https://doc.qt.io/qt-5/qscreen.html
        available_width = screen.availableGeometry().width()
        available_height = screen.availableGeometry().height()
        print(screen.availableSize())

        return int(available_width * width_fraction), int(available_height * height_fraction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
