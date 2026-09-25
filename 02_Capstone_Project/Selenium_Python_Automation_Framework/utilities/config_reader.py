from configparser import ConfigParser
from pathlib import Path


class ConfigReader:

    def __init__(self):
        project_root = Path(__file__).resolve().parents[1]
        config_path = project_root / "config" / "config.ini"

        self.config = ConfigParser()
        self.config.read(config_path)

    def get(self, key):
        return self.config["DEFAULT"][key]

    def get_int(self, key):
        return self.config["DEFAULT"].getint(key)

    def get_bool(self, key):
        return self.config["DEFAULT"].getboolean(key)
