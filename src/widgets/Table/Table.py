from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QWidget, QVBoxLayout, QPushButton, QLabel


class Table(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.table = QTableWidget()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # add row to table: https://stackoverflow.com/questions/6957943/how-to-add-new-row-to-existing-qtablewidget
        self.table.setColumnCount(3)
        self.table.insertRow(0)
        self.table.setItem(0, 1, QTableWidgetItem("vel x"))
        self.table.setItem(0, 2, QTableWidgetItem("vel y"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        table_title = QLabel("Tabla de velocidades")
        table_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(table_title)
        self.layout.addWidget(self.table)
        self.layout.addStretch()
        self.layout.addWidget(QPushButton("Obtener CSV"))

    def add_marker(self, marker_id: str):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(marker_id))

    def remove_marker(self, marker_id: int):
        self.table.removeRow(marker_id)
        for row in range(1, self.table.rowCount()):
            self.table.setItem(row, 0, QTableWidgetItem(str(row)))
