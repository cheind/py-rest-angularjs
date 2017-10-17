from flask import Flask
from flask import send_from_directory, make_response

app = Flask(__name__)


@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def basic_pages(**kwargs):
    return make_response(open('static/index.html').read())


@app.route('/api/')
def api():
    return 'Hello, World!'




if __name__ == "__main__":
    app.run(debug=True)