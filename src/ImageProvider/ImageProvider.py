import os
import numpy as np
import threading

import piv
import time

import PIL.TiffImagePlugin
from PIL import Image
from piv.model import Point, InputPIV

from src.MockedFiubaPIV.MockedFiubaPIV import MockedFiubaPIV
from src.constants.constants import Constants
from src.mainWindow import MainWindow


def get_image_list():
    path = os.path.join(os.path.dirname(__file__), "../../res/paired")
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


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

                self.send_image_to_GUI(left_half)
                self.send_image_to_backend(left_half, right_half)

    def read_image(self, img_number):
        im = Image.open(img_number)
        left_half, right_half = self.split_img(im)
        return left_half, right_half

    def send_image_to_GUI(self, new_img: PIL.TiffImagePlugin.TiffImageFile):
        if self.last_ui_refresh_timestamp_ns + int((1 / Constants.UI_REFRESH_RATE_IN_HZ) * 1e9) < time.time_ns():
            self.last_ui_refresh_timestamp_ns = time.time_ns()
            self.main_window.receive_img_from_img_reader(new_img)

    def split_img(self, new_img) -> (PIL.Image.Image, PIL.Image.Image):
        """
        split_img receives an img which contains two halves;
        it then splits original img in 2, and returns a tuple containing the two halves as separate imgs.
        """
        left_half_img = new_img.crop((get_crop_params_for_left_img(new_img.width, new_img.height)))  # PIL.Image.Image
        right_half_img = new_img.crop((get_crop_params_for_right_img(new_img.width, new_img.height)))  # PIL.Image.Image
        return left_half_img, right_half_img

    def send_image_to_backend(self, left_half: PIL.Image.Image, right_half: PIL.Image.Image):
        """
        new_img: whole img, which contains two imgs
        """
        if self.main_window.alg_running:
            points = {}
            for marker_id, marker_imgs in self.get_cropped_imgs(left_half.convert("L"),
                                                                right_half.convert("L"),
                                                                self.main_window.markers).items():
                marker = self.main_window.settings_bearer.settings[Constants.SETTINGS_MARKERS][marker_id]
                points[marker_id] = Point(marker['position_x'], marker['position_y'], marker_imgs)
            data = InputPIV(points,
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_DELTA_T],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_PPM],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_SELECTION_SIZE],
                            self.main_window.settings_bearer.settings[Constants.SETTINGS_ROI])
            piv_results = piv.calculate_piv(data)
            self.main_window.new_results(piv_results)

    def get_cropped_imgs(self, left_half: PIL.Image.Image, right_half: PIL.Image.Image, markers: dict) -> dict:
        """crop imgs of size of ROI, with marker centered in the area"""
        imgs = {}
        roi_value = self.main_window.settings_bearer.settings[Constants.SETTINGS_ROI]
        width, height = roi_value, roi_value
        for key in markers:
            x = markers[key]["position_x"]
            y = markers[key]["position_y"]
            left = x - (width // 2)
            top = y - (height // 2)
            right = left + width
            bottom = top + height
            left_half_crop = left_half.crop((left, top, right, bottom))  # PIL.Image.Image
            right_half_crop = right_half.crop((left, top, right, bottom))  # PIL.Image.Image
            imgs[key] = np.array([np.array(np.asarray(left_half_crop)), np.array(np.asarray(right_half_crop))])
        return imgs
