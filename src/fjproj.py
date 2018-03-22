#!/usr/bin/env python3
"""Fjproj: manage projects and shell environments"""
import sys
import os
import argparse
from fj.bash import call_bash
from fj.fjproj import load_projects, save_projects, edit_projects, list_projects
from fj.projpath import projpath

parser = argparse.ArgumentParser("Manage projects and shell environments")
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true')
group.add_argument('-d', '--delete', action='store_true')
group.add_argument('-e', '--edit', action='store_true')
group.add_argument('-n', '--new', action='store_true')
parser.add_argument('proj_name', nargs='?')
parser.add_argument('root_dir', nargs='?')


def activate_project(project_name):
    projects = load_projects()
    project = projects[project_name]
    proj_dir = os.path.expanduser(project['dir'])
    if project.get('default_bookmark'):
        workdir_relative_path = project['bookmarks'][project.get('default_bookmark')]
        workdir = os.path.join(proj_dir, workdir_relative_path)
    else:
        workdir = proj_dir
    os.chdir(workdir)
    os.environ['FJPROJ_CURRENT'] = project_name
    if project.get('activate') is not None:
        activate_path = os.path.expanduser(project['activate'])
        os.environ['FJPROJ_ACTIVATE'] = activate_path
    if project.get('paths') is not None:
        current_path = os.environ['PATH']
        os.environ['PATH'] = ':'.join([current_path] + project.get('paths'))
    call_bash(['--init-file', projpath('src', 'fj', 'fjproj_activate.sh')])

def create_project_obj(dir):
    return {'dir': dir}

def handle_main(argv):
    projects = load_projects()
    args = parser.parse_args(argv[1:])
    if args.list:
        list_projects(projects)
    elif args.new:
        name = args.proj_name
        dir = os.path.abspath(args.root_dir)
        assert name is not None, "Must specify project name"
        assert dir is not None, "Must specify project dir"
        if name in projects:
            raise KeyError("Project '{0}' already exists".format(name))
        if not os.path.exists(dir):
            os.mkdir(dir)
        projects[name] = create_project_obj(dir=dir)
        save_projects(projects)
    elif args.delete:
        assert args.proj_name is not None, "Must specify project name"
        del projects[args.proj_name]
        save_projects(projects)
    elif args.edit:
        edit_projects()
    elif args.proj_name:
        try:
            activate_project(args.proj_name)
        except KeyError:
            raise KeyError("No project matches '{0}'".format(args.proj_name))
    else:
        # No arguments
        list_projects(projects)

if __name__ == "__main__":
    handle_main(sys.argv)
