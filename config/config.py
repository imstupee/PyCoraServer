import yaml
import os
import sys

### CONSTANTS ###


if getattr(sys, 'frozen', False):  
    BASE_DIR = os.path.split(sys._MEIPASS)[0]
else:
    BASE_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  

CONFIG_FILE = "config.yaml"


### CONSTANTS ###


class ConfigLoader:
    def __init__(self):
        pass

    def load(self):
        data = self.read()
        if data:
            print(f"Read {data}")

            self.host = data.get("host")
            self.con_port = data.get("server_port")
            self.bcast_port = data.get("broadcast_port")
        else:
            print("Config file not found!")

    def read(self) -> dict:
        try:
            with open(os.path.join(BASE_DIR, CONFIG_FILE), "r") as config_file:
                config_data = yaml.full_load(config_file)
                return config_data
        except FileNotFoundError:
            return False
        
    def check(self):
        pass