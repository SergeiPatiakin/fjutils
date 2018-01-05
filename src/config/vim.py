"""Git configuration finder"""
from config.baseconfig import BaseConfig
from fj.projpath import appconfigpath, homepath

class VimConfig(BaseConfig):
    @staticmethod
    def get_config_files():
        theirs_path = appconfigpath("vim", "vimrc")
        yours_path = homepath(".vimrc")
        return [yours_path], [theirs_path]