"""Determine platform"""
import sys

if sys.platform in ("linux", "linux2"):
    platform = "linux"
elif sys.platform == "darwin":
    platform = "mac"
elif sys.platform == "win32":
    platform = "windows"
else:
    raise Exception("Unknown environment: {0}. No idea how to proceed.".format(
        sys.platform))
