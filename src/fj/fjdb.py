"""Bare bones JSON-based registry"""
import os
from .projpath import dbpath
import json

def load(name, default_type = 'list'):
    object_path = get_file(name)
    if os.path.exists(object_path):
        with open(object_path) as object_file:
            return json.loads(object_file.read())
    else:

        if default_type == 'list':
            return []
        elif default_type == 'dict':
            return {}
        else:
            raise NotImplementedError()

def get_file(name):
    return dbpath(name + '.json')

def save(name, data):
    db_path = dbpath(name + '.json')
    with open(db_path, 'w') as db_file:
        db_file.write(json.dumps(data, indent=4))

db_dir = dbpath()
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
