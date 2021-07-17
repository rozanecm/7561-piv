import threading
import time

from src.mainWindow import MainWindow


class ImageProvider(threading.Thread):
    def __init__(self, main_window: MainWindow):
        threading.Thread.__init__(self, daemon=True)
        self.markers_info = {}
        self.main_window = main_window

    def run(self):
        img_number = 1
        while True:
            time.sleep(1)
            new_img = self.read_image(img_number)
            img_number += 1

            self.send_image_to_GUI(new_img)
            self.send_image_to_backend(new_img)

    def read_image(self, img_number):
        print("read img n", img_number)
        return "img {}".format(img_number)

    def send_image_to_GUI(self, new_img):
        self.main_window.receive_img_from_imag_reader(new_img)

    def send_image_to_backend(self, new_img):
        if not self.markers_info:
            print("sending img to backend", new_img)
            # self.main_window.get_markers_info()
