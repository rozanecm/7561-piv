import sys

from PyQt5.QtWidgets import QApplication

from src.ImageProvider.ImageProvider import ImageProvider
from src.mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow(app=app)
    image_provider = ImageProvider(main_window)
    image_provider.start()
    # Explanation on exec_() vs exec() options: https://www.xspdf.com/resolution/54849147.html
    sys.exit(app.exec_())
