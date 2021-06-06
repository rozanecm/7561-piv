import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGraphicsPixmapItem, QGraphicsItem, QLabel, QVBoxLayout, \
    QPushButton
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter, QPen


class ImageWidget(QWidget):
    # inspired by: https://stackoverflow.com/questions/45018926/how-to-properly-setpixmap-scaled-on-pyqt5
    # which also shows how to draw something on the img!
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.pixmap = QPixmap("icon.png")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_size()
        self.setWindowTitle('PIV')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        # box layout docs: https://doc.qt.io/qt-5/qboxlayout.html
        self.setLayout(QHBoxLayout())
        label = ImageWidget()
        # 2nd arg. is expected: it's the stretch factor
        self.layout().addWidget(label, 5)
        self.layout().addWidget(QPushButton(), 2)

        self.show()

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
