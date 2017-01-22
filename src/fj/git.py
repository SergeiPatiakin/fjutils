"""Functions for working with Git repositories"""
import subprocess
import os
import re


def get_repo_dir():
    return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                            stdout=subprocess.PIPE).communicate()[
        0].rstrip().decode('utf-8')


def create_symref(alias_ref, target_ref):
    subprocess.call(['git', 'symbolic-ref', 'refs/heads/{0}'.format(alias_ref),
                     'refs/heads/{0}'.format(target_ref)])

def delete_symref(alias_ref):
    subprocess.call(['git', 'symbolic-ref', '-d',
                     'refs/heads/{0}'.format(alias_ref)])

def list_symrefs():
    heads_dir = os.path.join(get_repo_dir(), '.git', 'refs', 'heads')
    refs_list = []
    for dir_entry in os.listdir(heads_dir):
        full_path = os.path.join(heads_dir, dir_entry)
        if os.path.isfile(full_path):
            ref = open(full_path, 'r').read()
            match = re.match("ref: refs/heads/(.*)", ref)
            if match is not None:
                refs_list.append(dir_entry)
    for r in refs_list:
        print(r)

def get_current_branch():
    head_file = os.path.join(get_repo_dir(), '.git', 'HEAD')
    head_ref = open(head_file, 'r').read()
    match = re.match("ref: refs/heads/(.*)", head_ref)
    if match is None:
        return None
    else:
        cur_branch = match.group(1)
        return cur_branch
