import os
import threading

import PIL.TiffImagePlugin
import time
from PIL import Image

from src.MockedFiubaPIV.MockedFiubaPIV import MockedFiubaPIV
from src.constants.constants import Constants
from src.mainWindow import MainWindow


def get_image_list():
    path = os.path.join(os.path.dirname(__file__), "../../res/paired")
    paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return sorted(paths)


def get_crop_params_for_left_img(width: int, height: int) -> (int, int, int, int):
    left = 0
    top = 0
    right = width // 2
    bottom = height
    return left, top, right, bottom


def get_crop_params_for_right_img(width: int, height: int) -> (int, int, int, int):
    left = width // 2
    top = 0
    right = width
    bottom = height
    return left, top, right, bottom


class ImageProvider(threading.Thread):
    def __init__(self, main_window: MainWindow):
        threading.Thread.__init__(self, daemon=True)
        self.markers_info = {}
        self.main_window = main_window
        self.images_paths = get_image_list()
        self.fiuba_piv = MockedFiubaPIV()
        self.last_ui_refresh_timestamp_ns = time.time_ns()

    def run(self):
        while True:
            for current_img_path in self.images_paths:
                time.sleep(1 / Constants.IMAGE_INPUT_FRECUENCY_IN_HZ)
                left_half, right_half = self.read_image(current_img_path)

                self.send_image_to_GUI(left_half, right_half)

    def read_image(self, img_number):
        im = Image.open(img_number)
        left_half, right_half = self.split_img(im)
        return left_half, right_half

    def send_image_to_GUI(self, left_half: PIL.TiffImagePlugin.TiffImageFile, right_half: PIL.TiffImagePlugin.TiffImageFile):
        self.main_window.send_image_to_backend(left_half, right_half)
        if self.last_ui_refresh_timestamp_ns + int((1 / Constants.UI_REFRESH_RATE_IN_HZ) * 1e9) < time.time_ns():
            self.last_ui_refresh_timestamp_ns = time.time_ns()
            self.main_window.receive_img_from_img_reader(left_half)

    def split_img(self, new_img) -> (PIL.Image.Image, PIL.Image.Image):
        """
        split_img receives an img which contains two halves;
        it then splits original img in 2, and returns a tuple containing the two halves as separate imgs.
        """
        left_half_img = new_img.crop((get_crop_params_for_left_img(new_img.width, new_img.height)))  # PIL.Image.Image
        right_half_img = new_img.crop((get_crop_params_for_right_img(new_img.width, new_img.height)))  # PIL.Image.Image
        return left_half_img, right_half_img
