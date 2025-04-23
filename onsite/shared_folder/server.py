
from flask import Flask, send_from_directory, render_template_string, abort
import os

app = Flask(__name__)

# Change this to your shared root folder path
BASE_DIR = os.path.abspath("shared_folder")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>File Server</title>
</head>
<body>
    <h1>Index of: /{{ rel_path }}</h1>
    {% if rel_path %}
    <a href="{{ url_for('browse', path=rel_path.rsplit('/', 1)[0]) }}">[Parent Directory]</a><br>
    {% endif %}
    <ul>
    {% for name, is_dir in items %}
        <li>
        {% if is_dir %}
            <a href="{{ url_for('browse', path=(rel_path + '/' + name).strip('/')) }}">{{ name }}/</a>
        {% else %}
            <a href="{{ url_for('download_file', path=(rel_path + '/' + name).strip('/')) }}">{{ name }}</a>
        {% endif %}
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def browse(path):
    abs_path = os.path.abspath(os.path.join(BASE_DIR, path))

    # Prevent directory traversal
    if not abs_path.startswith(BASE_DIR):
        abort(403)

    if os.path.isdir(abs_path):
        items = sorted([(name, os.path.isdir(os.path.join(abs_path, name)))
                        for name in os.listdir(abs_path)])
        return render_template_string(HTML_TEMPLATE, items=items, rel_path=path)
    else:
        return download_file(path)

@app.route('/download/<path:path>')
def download_file(path):
    abs_path = os.path.abspath(os.path.join(BASE_DIR, path))

    if not abs_path.startswith(BASE_DIR):
        abort(403)

    directory = os.path.dirname(abs_path)
    filename = os.path.basename(abs_path)
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
