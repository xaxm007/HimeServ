import os
from os.path import expanduser, isdir, isfile, join

current_path = os.getcwd()

folders = {}
files = {}

for item in os.listdir(current_path):
    if isdir(item):
        # folders.append({item : f'{join(current_path, item)}'})
        folders.update({item : join(current_path, item)})

    # if isfile(item):
        # files.append({item : f'{join(current_path, item)}'})

for folder, folder_path in folders.items():
    print(folder, folder_path)
    # print(folder.keys())
    # type(folder.keys())

print(current_path)
