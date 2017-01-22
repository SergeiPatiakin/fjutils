#!/usr/bin/env python3
"""Fjproj: manage projects and shell environments"""
import sys
import os
import argparse
from fj.fjdb import load, save, get_file
from fj.editor import DefaultEditor
from fj.projpath import projpath
from subprocess import call

parser = argparse.ArgumentParser("Manage projects and shell environments")
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true')
group.add_argument('-d', '--delete', action='store_true')
group.add_argument('-e', '--edit', action='store_true')
group.add_argument('-n', '--new', action='store_true')
parser.add_argument('proj_name', nargs='?')
parser.add_argument('root_dir', nargs='?')

def load_projects():
    return load("projects", default_type='dict')

def save_projects(projects):
    save("projects", projects)

def edit_projects():
    DefaultEditor.simple_open(get_file("projects"))

def list_projects(projects):
    for project_name in projects:
        print(project_name)

def activate_project(project_name):
    projects = load_projects()
    project = projects[project_name]
    workdir = os.path.expanduser(project['dir'])
    os.chdir(workdir)
    os.environ['FJPROJ_CURRENT'] = project_name
    if project.get('activate') is not None:
        activate_path = os.path.expanduser(project['activate'])
        os.environ['FJPROJ_ACTIVATE'] = activate_path
    call(['bash', '--init-file', projpath('src', 'fj', 'fjproj_activate.sh')])

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
