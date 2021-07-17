import os
import threading
import time
from PIL import Image

from src.mainWindow import MainWindow


def get_image_list():
    path = os.path.join(os.path.dirname(__file__), "../../res/piv_imgs")
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


class ImageProvider(threading.Thread):
    def __init__(self, main_window: MainWindow):
        threading.Thread.__init__(self, daemon=True)
        self.markers_info = {}
        self.main_window = main_window
        self.images_paths = get_image_list()

    def run(self):
        while True:
            for current_img_path in self.images_paths:
                time.sleep(1)
                new_img = self.read_image(current_img_path)

                self.send_image_to_GUI(new_img)
                self.send_image_to_backend(new_img)

    def read_image(self, img_number):
        print("read img", img_number)
        im = Image.open(img_number)
        print(im.format, im.size, im.mode)
        return im
        # return "img {}".format(img_number)

    def send_image_to_GUI(self, new_img):
        self.main_window.receive_img_from_imag_reader(new_img)

    def send_image_to_backend(self, new_img):
        if not self.markers_info:
            print("sending img to backend", new_img)
            # self.main_window.get_markers_info()
