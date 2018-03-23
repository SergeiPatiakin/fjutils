import os
from os.path import isfile, islink, join
from fj.projpath import INSTALL_ROOT, SCRIPT_BIN_DIR
from fj.environment import platform

SCRIPT_ROOT = os.path.join(INSTALL_ROOT, 'src')

def rebuild_script_links():
    """Build symlinks to allow script invocation without the '.py' extension"""
    # Remove links
    for dir_entry in os.listdir(SCRIPT_BIN_DIR):
        full_path = join(SCRIPT_BIN_DIR, dir_entry)
        if islink(full_path): os.remove(full_path)

    # Rebuild links
    if platform != "windows":
        for dir_entry in os.listdir(SCRIPT_ROOT):
            full_source_path = join(SCRIPT_ROOT, dir_entry)
            command_name = dir_entry[:-3]
            full_dest_path = join(SCRIPT_BIN_DIR, command_name)
            if isfile(full_source_path) and dir_entry != "__init__.py":
                if full_source_path.endswith('.py') or full_source_path.endswith('.sh'):
                    os.symlink(full_source_path, full_dest_path)
