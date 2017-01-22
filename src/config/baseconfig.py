"""Base class for configuration finders"""
class BaseConfig:
    @staticmethod
    def get_config_files():
        """Subclasses should implement this method, returning a 2-tuple (yours_list, theirs_list).
            yours_list is a list of configuration paths on this system.
            theirs_list is a list of configuration templates available from fjutils
        """
        raise NotImplementedError()
