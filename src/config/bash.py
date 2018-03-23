"""Bash configuration finder"""
from config.baseconfig import BaseConfig
from fj.projpath import appconfigpath, homepath
from fj.environment import platform


class BashConfig(BaseConfig):
    @staticmethod
    def get_config_files():
        theirs_path = appconfigpath("bash", "bashprofile")
        yours_path = homepath(".profile"
                              if platform == 'linux' else ".bash_profile")
        return [yours_path], [theirs_path]
