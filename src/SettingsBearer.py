from typing import Union

from src.constants.constants import Constants


class SettingsBearer:
    def __init__(self):
        self.settings = {}

    def update_settings(self, msg_type: Constants, body: Union[str, dict]):
        self.settings[msg_type] = body
        print("settings updated - new settings: {}".format(self.settings))
