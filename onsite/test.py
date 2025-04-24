import os
from os.path import expanduser, isdir, isfile, join

BASE_DIR = expanduser("~")


def home_surf(path):
    folders = {}
    files = {}

    if not path == '':
        current_path = path
    else:
        current_path = join(BASE_DIR, path)

    folders = {}
    files = {}

    for item in os.listdir(current_path):
        if not item.startswith('.'):
            item_path = join(current_path, item)

            if isdir(item_path):
                folders.update({item : item_path})

            if isfile(item_path):
                files.update({item : item_path})

    return folders, files

traverse = input()
print(home_surf(traverse))
