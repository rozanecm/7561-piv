from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy

from src.widgets.CircleMarker.CircleMarker import CircleMarker


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
