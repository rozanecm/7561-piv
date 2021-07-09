from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QWidget, QVBoxLayout, QLabel, QHeaderView


class Table(QWidget):
    _marker_id_column_index = 0
    _vel_x_column_index = 1
    _vel_y_column_index = 2
    _pos_x_column_index = 3
    _pos_y_column_index = 4

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.table_title = QLabel()
        self.table = QTableWidget()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_table()

        self.layout.addWidget(self.table_title)
        self.layout.addWidget(self.table)
        self.layout.addStretch()

    def init_table(self):
        # add row to table: https://stackoverflow.com/questions/6957943/how-to-add-new-row-to-existing-qtablewidget
        self.table.setColumnCount(5)
        self.table.insertRow(0)
        self.table.setItem(0, 1, QTableWidgetItem("vel x"))
        self.table.setItem(0, 2, QTableWidgetItem("vel y"))
        self.table.setItem(0, 3, QTableWidgetItem("pos x"))
        self.table.setItem(0, 4, QTableWidgetItem("pos y"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_title.setText("Velocidades instantáneas")
        self.table_title.setAlignment(Qt.AlignCenter)

        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def add_marker(self, marker_id: str, pos_x: int, pos_y: int):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.get_last_row_index(), self._marker_id_column_index, QTableWidgetItem(marker_id))
        self.table.setItem(self.get_last_row_index(), self._pos_x_column_index, QTableWidgetItem(str(pos_x)))
        self.table.setItem(self.get_last_row_index(), self._pos_y_column_index, QTableWidgetItem(str(pos_y)))

    def get_last_row_index(self):
        return self.table.rowCount() - 1

    def remove_marker(self, marker_id: int):
        self.table.removeRow(marker_id)
        for row in range(1, self.table.rowCount()):
            self.table.setItem(row, self._marker_id_column_index, QTableWidgetItem(str(row)))
