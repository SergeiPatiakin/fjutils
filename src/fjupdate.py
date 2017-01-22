#!/usr/bin/env python3
"""Update fjutils installation from upstream"""
from fj.projpath import chdir_install_root
from fj.scriptlinks import rebuild_script_links
import subprocess

if __name__ == "__main__":
    chdir_install_root()
    subprocess.call(['git', 'pull'])
    rebuild_script_links()
