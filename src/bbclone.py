#!/usr/bin/env python3
"""Clone a bitbucket repo"""
import sys
import argparse
from fj.fjdb import load
from fj.git import call_git

parser = argparse.ArgumentParser("bbc")
parser.add_argument('reponame')
parser.add_argument('dirname', nargs='?', type=str)

def main(argv):
    args = parser.parse_args(argv)
    reponame = args.reponame
    fjutils_conf = load("fjutils", default_type='dict')
    bitbucket_username = fjutils_conf.get('bitbucket_username')
    git_args = ['clone', 'https://{0}@bitbucket.org/{0}/{1}.git'.format(bitbucket_username, reponame), '-o', 'bitbucket']
    if args.dirname is not None:
        git_args.append(args.dirname)
        call_git(git_args)

if __name__ == "__main__":
    main(sys.argv[1:])
