import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

# Add handler that just prints to stdout
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)