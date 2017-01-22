#!/usr/bin/env python3
"""Fjconf: manage app configurations"""
import sys
import argparse
from config.git import GitConfig
from config.subl3 import Subl3Config
from config.bash import BashConfig
from fj.nameresolver import NameResolver
from fj.editor import DefaultEditor

config_classes = NameResolver({
    GitConfig: ['git'],
    Subl3Config: ['subl', 'subl3'],
    BashConfig: ['bash'],
})

parser = argparse.ArgumentParser(description='Manage app configurations')
parser.add_argument('-e', '--edit', action='store_true')
parser.add_argument('app_name', nargs='?')
parser.add_argument('yours_num', nargs='?', type=int)
parser.add_argument('theirs_num', nargs='?', type=int)

def list_apps():
    print("Supported apps:")
    for name, _ in config_classes.items():
        print('    '+name)

def list_app_configs(app):
    if app in config_classes:
        config_class = config_classes[app]
        yours_list, theirs_list = config_class.get_config_files()
        print("Your config files for '{0}':".format(app))
        for idx, path in enumerate(yours_list): print('    {0}: {1}'.format(idx+1, path))
        print("Fjutils config files for '{0}':".format(app))
        for idx, path in enumerate(theirs_list): print('    {0}: {1}'.format(idx+1, path))
    else:
        raise KeyError(app)

def edit_app_config(app, yours_idx_str=None, theirs_idx_str=None):
    if app in config_classes:
        config_class = config_classes[app]
        yours_list, theirs_list = config_class.get_config_files()
        if (yours_idx_str is None):
            if len(yours_list)>1: raise ValueError('Multiple configs available. Must specify config numbers for yours and theirs')
            else: yours_idx_str = '1'
        if (theirs_idx_str is None):
            if len(theirs_list)>1: raise ValueError('Multiple configs available. Must specify config numbers for yours and theirs')
            else: theirs_idx_str = '1'
        yours_idx = int(yours_idx_str)-1
        theirs_idx = int(theirs_idx_str)-1
        # TODO: maybe this should be moved to BaseConfig, so that subclasses can customize? E.g. PyCharm
        DefaultEditor.compare(yours_list[yours_idx], theirs_list[theirs_idx])
    else:
        raise KeyError(app)

def handle_main(argv):
    args = parser.parse_args(argv[1:])
    if args.edit:
        assert args.app_name, "Must specify app name"
        if args.yours_num is not None and args.theirs_num is not None:
            edit_app_config(args.app_name, args.yours_num, args.theirs_num)
        else:
            edit_app_config(args.app_name)
    elif args.app_name:
        # List configs for app_name
        list_app_configs(args.app_name)
    else:
        # List available apps
        list_apps()

if __name__ == "__main__":
    handle_main(sys.argv)
