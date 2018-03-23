"""Path utils"""
import os


def appconfigpath(*path):
    return os.path.join(INSTALL_ROOT, 'configtemplates', *path)


def projpath(*path):
    return os.path.join(INSTALL_ROOT, *path)


def homepath(*path):
    return os.path.join(USER_HOME, *path)


def dbpath(*path):
    return homepath('.config', 'fjutils', *path)


def chdir_install_root():
    os.chdir(INSTALL_ROOT)


USER_HOME = os.path.expanduser("~")
INSTALL_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SCRIPT_BIN_DIR = os.path.join(INSTALL_ROOT, 'bin')
