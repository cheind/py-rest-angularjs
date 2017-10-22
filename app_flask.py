"""
AngularJS / Python backend

This script uses flask for the backend. Make sure to have flask installed,
then run `python app_flask.py` from the directory this file is contained in.
"""

from flask import Flask
from flask import send_from_directory, make_response, jsonify

app = Flask(__name__)

@app.route('/vendor/<path:path>')
def serve_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Note, any AngularJS local route should also be added here.
# Otherwise, calling the route directly will not allow AngularJS
# to handle it safely.
@app.route('/')
def serve_index():
    return make_response(open('static/index.html').read())

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify(message='Hello {}'.format(name))

if __name__ == "__main__":
    app.run(debug=True)