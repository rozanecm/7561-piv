import sys

from PyQt5.QtWidgets import QApplication

from src.mainWindow import MainWindow

# sample empty widget
# src: https://www.geeksforgeeks.org/creating-custom-widgets-in-pyqt5/
# class MyWidget(QtWidgets.QWidget):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.layout = QtWidgets.QGridLayout()
# 		self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow(app=app)
    sys.exit(app.exec_())
