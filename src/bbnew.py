#!/usr/bin/env python3
"""Create a bitbucket repo and add it as a remote"""
import sys
import argparse
import getpass
from fj.bitbucket import bitbucket_create
from fj.fjdb import load
from fj.git import call_git

parser = argparse.ArgumentParser("bbc")
parser.add_argument('reponame')


def main(argv):
    args = parser.parse_args(argv)
    reponame = args.reponame
    fjutils_conf = load("fjutils", default_type='dict')
    bitbucket_username = fjutils_conf.get('bitbucket_username')
    bitbucket_password = fjutils_conf.get('bitbucket_password')
    if not bitbucket_username:
        print("Bitbucket credentials not found in config.")
        bitbucket_username = input("Bitbucket username: ")
    if not bitbucket_password:
        bitbucket_password = getpass.getpass('Bitbucket password: ')
    bitbucket_create(bitbucket_username, reponame, bitbucket_password)
    call_git([
        'remote', 'add',
        'bitbucket', 'https://{0}@bitbucket.org/{0}/{1}.git'.format(
            bitbucket_username, reponame)
    ])


if __name__ == "__main__":
    main(sys.argv[1:])
