import os
from flask import Flask, send_from_directory, request
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='/build', static_folder="build")

CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists("build/" + path):
        return send_from_directory('build', path)
    elif path != "" and path.startswith("static"):
        if path.startswith("static/js"):
            for f in os.listdir(os.path.join(app.static_folder, "static/js")):
                if f.endswith(".js"):
                    return send_from_directory('build', "static/js/" + f)
        elif path.startswith("static/css"):
            for f in os.listdir(os.path.join(app.static_folder, "static/css")):
                if f.endswith(".css"):
                    return send_from_directory('build', "static/css/" + f)
    else:
        return send_from_directory('build', 'index.html')


if __name__ == "__main__":
    port = 3360
    if os.environ.get('PORT'):
        port = int(os.environ.get('PORT'))
    app.run(port=port, host='0.0.0.0')