#!/usr/bin/env python3
"""Gitshort: Create, list and delete aliases for git branches."""
import sys
import argparse
from fj.git import get_current_branch, create_symref, delete_symref, \
    list_symrefs

parser = argparse.ArgumentParser(description='Create, list and delete aliases for git branches.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--delete', action='store_true')
group.add_argument('-l', '--list', action='store_true')
parser.add_argument('ref_name', nargs='?')

def gitshort(argv):
    args = parser.parse_args(argv[1:])
    if args.delete:
        if not args.ref_name:
            raise Exception('Must specify ref to delete')
        delete_symref(args.ref_name)
    elif args.list:
        list_symrefs()
    elif args.ref_name:
        cur_branch = get_current_branch()
        if not cur_branch:
            raise Exception("Repository is in detached head state")
        else:
            create_symref(args.ref_name, cur_branch)
    else:
        # No arguments
        list_symrefs()

if __name__ == "__main__":
    gitshort(sys.argv)
