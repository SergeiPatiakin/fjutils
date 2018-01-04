#!/usr/bin/env python3

import sys
import os
import argparse
from fjproj import load_projects
from fj.bash import bash_quote

parser = argparse.ArgumentParser("Navigate to bookmarks within a project")
parser.add_argument('bookmark', nargs='?')

def main(argv):
    args = parser.parse_args(argv)
    project_name = os.environ.get('FJPROJ_CURRENT')
    projects = load_projects()
    project = projects[project_name]
    proj_dir = os.path.expanduser(project['dir'])
    if args.bookmark is not None:
        workdir_relative_path = project['bookmarks'][args.bookmark]
        workdir = os.path.join(proj_dir, workdir_relative_path)
    else:
        workdir = proj_dir
    print("cd '{0}'".format(bash_quote(workdir)))

if __name__ == "__main__":
    main(sys.argv[1:])