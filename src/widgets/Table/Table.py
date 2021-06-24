from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView


class Table(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # add row to table: https://stackoverflow.com/questions/6957943/how-to-add-new-row-to-existing-qtablewidget
        self.setColumnCount(3)
        self.insertRow(0)
        self.setItem(0, 1, QTableWidgetItem("vel x"))
        self.setItem(0, 2, QTableWidgetItem("vel y"))
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def remove_marker(self, marker_id: int):
        self.removeRow(marker_id)
        for row in range(1, self.rowCount()):
            self.setItem(row, 0, QTableWidgetItem(str(row)))
