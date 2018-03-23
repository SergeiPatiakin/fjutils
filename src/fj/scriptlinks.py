import os
from os.path import isfile, islink, join
from fj.projpath import SCRIPT_ROOT
from fj.environment import platform


def rebuild_script_links():
    """Build symlinks to allow script invocation without the '.py' extension"""
    # Remove links
    for dir_entry in os.listdir(SCRIPT_ROOT):
        full_path = join(SCRIPT_ROOT, dir_entry)
        if islink(full_path): os.remove(full_path)

    # Rebuild links
    if platform != "windows":
        for dir_entry in os.listdir(SCRIPT_ROOT):
            full_path = join(SCRIPT_ROOT, dir_entry)
            if isfile(full_path) and dir_entry != "__init__.py":
                if full_path.endswith('.py') or full_path.endswith('.sh'):
                    os.symlink(full_path, full_path[:-3])
