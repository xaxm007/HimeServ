from flask import Flask, render_template, request
import os
from os.path import expanduser, isdir, isfile, join, abspath

BASE_DIR = os.getcwd()
# HOME_DIR = expanduser("~")
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home_surf(path):

    current_path = abspath(join(BASE_DIR, path))
    print(current_path)

    if not current_path.startswith(BASE_DIR):
        return "Access Denied", 403

    folders = {}
    files = {}

    for item in os.listdir(current_path):
        if not item.startswith('.'):
            item_path = join(current_path, item)
            if isdir(item_path):
                folders.update({item : item_path})

            if isfile(item_path):
                files.update({item : item_path})

    return render_template('files.html', folders=folders, files=files)
