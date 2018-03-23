"""Sublime Text 3 configuration finder"""
from config.baseconfig import BaseConfig
from fj.projpath import appconfigpath, homepath
from fj.environment import platform
import os


class Subl3Config(BaseConfig):
    @staticmethod
    def get_config_files():
        theirs_path = appconfigpath("subl3", "Preferences.sublime-settings")
        if platform == "windows":
            app_data_root = os.getenv('APPDATA')
            yours_path = os.path.join(app_data_root, 'Sublime Text 3',
                                      "Packages", "User",
                                      "Preferences.sublime-settings")
        else:
            yours_path = homepath(".config", "sublime-text-3", "Packages",
                                  "User", "Preferences.sublime-settings")
        return [yours_path], [theirs_path]
