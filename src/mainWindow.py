from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QImage, QColor, QPen
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QButtonGroup, QCheckBox, QVBoxLayout, QSizePolicy, \
    QHBoxLayout

from src.widgets.tabs.tabs_widget import TabWidget
from src.widgets.CircleMarker.CircleMarker import CircleMarker


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



class ImageWidget(QWidget):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    #
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        path = "res/icon.png"

        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap(path))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.layout.addWidget(self.imageLabel)

        self.show()

    # def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        print("hehe")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}; current size: {}".format(x, y, self.size()))
        print("widget size:", self.frameSize())
        asdf = CircleMarker(1, parent=self)
        asdf.move(x, y)
        asdf.show()
        self.update()

    def getPos(self, event):
        print("vnm")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}".format(x, y))


class MainWindow(QWidget):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.layout = QVBoxLayout()
        self.init_gui()

    def init_gui(self):
        self.set_size()
        self.setWindowTitle('PIV')
        self.setWindowIcon(QtGui.QIcon('../res/icon.png'))

        self.setLayout(self.layout)
        self.layout.addWidget(ImageWidget())
        self.layout.addWidget(TabWidget())

        self.show()

    def set_size(self):
        minimum_size = self.get_minimum_size()
        self.setMinimumSize(minimum_size[0], minimum_size[1])

    def get_minimum_size(self, width_fraction=0.9, height_fraction=0.8):
        """
        :return min_width, min_height of the window.
        :argument width_fraction: the amount of the available width the actual screen will take
        :argument height_fraction: the amount of the available height the actual screen will take
        """
        screen = self.app.primaryScreen()

        # for more screen properties available: https://doc.qt.io/qt-5/qscreen.html
        available_width = screen.availableGeometry().width()
        available_height = screen.availableGeometry().height()
        print(screen.availableSize())

        return int(available_width * width_fraction), int(available_height * height_fraction)
