from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QVBoxLayout

from src.widgets.ImageWidget.ImageWidget import ImageWidget
from src.widgets.tabs.tabs_widget import TabWidget
from src.widgets.tabsContent.tab_content_widget import TabContent


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


class MainWindow(QWidget):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.points = {}

        self.image_widget = ImageWidget(parent=self)
        self.tab_widget = TabWidget(parent=self)

        self.init_gui()

    def init_gui(self):
        self.set_size()
        self.setWindowTitle('PIV')
        self.setWindowIcon(QtGui.QIcon('../res/icon.png'))
        self.layout.addWidget(self.image_widget)
        self.layout.addWidget(self.tab_widget)

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

    def add_point(self, position_x: int = 0, position_y: int = 0, selection_size: int = 32):
        new_point_id = self.get_new_point_id()
        self.tab_widget.tabWidget.addTab(
            TabContent(main_window=self, point_id=new_point_id, position_x=position_x, position_y=position_y),
            str(new_point_id))
        self.image_widget.add_point(position_x,
                                    position_y,
                                    new_point_id)
        self.points[new_point_id] = {"position_x": position_x,
                                     "position_y": position_y,
                                     "selection_size": selection_size}
        # focus on the last created tab.
        self.tab_widget.tabWidget.setCurrentIndex(self.tab_widget.tabWidget.count() - 1)
        if len(self.points.keys()) > 1:
            self.tab_widget.quitar_punto_button.setEnabled(True)

    def get_new_point_id(self) -> int:
        return 1 if len(self.points.keys()) == 0 else max(self.points.keys()) + 1

    def update_position_from_image(self, point_id: int, new_x: int, new_y: int):
        # focus on updating tab.
        self.tab_widget.tabWidget.setCurrentIndex(point_id - 1)
        self.tab_widget.tabWidget.widget(point_id - 1).update_position(new_x, new_y)

    def update_position_from_tab(self, point_id: int, new_x: int, new_y: int):
        self.image_widget.update_position_from_tab(point_id, new_x, new_y)
