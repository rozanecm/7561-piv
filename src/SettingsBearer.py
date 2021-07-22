from typing import Union

from src.constants.constants import Constants


class SettingsBearer:
    def __init__(self):
        self.settings = {"markers": {}}

    def update_settings(self, msg_type: Constants, body: Union[str, dict]):
        self.settings[msg_type] = body
        print("settings updated - new settings: {}".format(self.settings))

    def new_marker_settings(self, info: dict):
        self.settings[Constants.SETTINGS_MARKERS][info["marker_id"]] = (info["pos_x"], info["pos_y"])
        print("settings updated after new marker - new settings: {}".format(self.settings))

    def update_marker_settings(self, info: dict):
        self.settings[Constants.SETTINGS_MARKERS][info["marker_id"]] = (info["pos_x"], info["pos_y"])
        print("settings updated after new marker new pos - new settings: {}".format(self.settings))
