from fj.fjdb import load, save, get_file
from fj.editor import DefaultEditor


def load_projects():
    return load("projects", default_type='dict')


def save_projects(projects):
    save("projects", projects)


def edit_projects():
    DefaultEditor.simple_open(get_file("projects"))


def list_projects(projects, stream=None):
    for project_name in projects:
        if stream is None:
            print(project_name)
        else:
            stream.write(project_name + '\n')
