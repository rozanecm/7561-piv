from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from src.widgets.CircleMarker.CircleMarker import CircleMarker


class ImageWidget(QWidget):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    #
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        path = "res/sample_cropped.png"

        self.imageLabel = QLabel()
        self.set_image(path)

        self.layout.addWidget(self.imageLabel)

        self.show()

    def set_image(self, path):
        # docs to understand pixmap scaling: https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html#PySide6.QtGui.PySide6.QtGui.QPixmap.scaled
        if self.imageLabel.size().width() > self.imageLabel.size().height():
            self.imageLabel.setPixmap(
                QPixmap(path).scaled(self.imageLabel.size().width(), self.imageLabel.size().width(),
                                     QtCore.Qt.KeepAspectRatio))
        else:
            self.imageLabel.setPixmap(
                QPixmap(path).scaled(self.imageLabel.size().width(), self.imageLabel.size().width(),
                                     QtCore.Qt.KeepAspectRatio))

    # def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        print("hehe")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}; current size: {}".format(x, y, self.size()))
        print("widget size:", self.frameSize())
        self.parent().add_point(x, y)

    def add_point(self, x, y):
        new_point = CircleMarker(parent=self)
        new_point.move(x, y)
        new_point.show()
        self.update()

    def getPos(self, event):
        print("vnm")
        x = event.pos().x()
        y = event.pos().y()
        print("x: {}, y: {}".format(x, y))
