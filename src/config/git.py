"""Git configuration finder"""
from config.baseconfig import BaseConfig
from fj.projpath import appconfigpath, homepath


class GitConfig(BaseConfig):
    @staticmethod
    def get_config_files():
        theirs_path = appconfigpath("git", "gitconfig")
        yours_path = homepath(".gitconfig")
        return [yours_path], [theirs_path]
