import json
import logging

from src.constants.constants import Constants


class InfoOutputter():
    LOG_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s"
    # LOG_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d"

    def __init__(self):
        self.logger = logging.getLogger("logger")
        logging.basicConfig(format=self.LOG_FORMAT)
        self.logger.setLevel(logging.DEBUG)

    def transmit_message(self, msg_type: Constants, body: str):
        msg = {msg_type: body}
        self.logger.info(json.dumps(msg, indent=4))
