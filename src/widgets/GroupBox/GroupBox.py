from PyQt5.QtWidgets import QGroupBox


class GroupBox(QGroupBox):
    def __init__(self, title: str, parent=None):
        super().__init__(parent=parent)
        self.setTitle(title)
        # groupbox style: https://stackoverflow.com/questions/42655988/adjust-title-position-in-a-qgroupbox-using-style-sheets  # noqa: E501
        # How to use groupbox style title and box separately: https://stackoverflow.com/questions/40043709/how-to-customise-qgroupbox-title-in-pyqt5    # noqa: E501
        self.setStyleSheet("""
                QGroupBox{
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 6px;
                }
                QGroupBox:title{
                    subcontrol-origin: margin;
                    left: 7px;
                    padding: 0px 5px 0px 5px;
                }
                """)
