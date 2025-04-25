from flask import Flask, render_template, send_from_directory
import os
from os.path import expanduser, isdir, isfile, join, abspath

# BASE_DIR = os.getcwd()
BASE_DIR = expanduser("~")
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home_surf(path):

    # current_path = abspath(join(BASE_DIR, path))
    if not path == '':
        current_path = join('/', path)
    else:
        current_path = join(BASE_DIR, path)

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

    return render_template('directory.html', folders=folders, files=files)

@app.route('/display/<path:path>')
def display_file(path):
    path = join('/', path)
    if isfile(path):
        filename = path.split('/')[-1]
        try:
            with open(path, 'r') as file:
                content = file.read()
        except Exception as e:
            content = f"Error: {e}"

    return render_template('file.html', content=content, filename=filename)

    # return send_from_directory()

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content, tells browser: nothing to see here
