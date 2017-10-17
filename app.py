from flask import Flask
from flask import send_from_directory, make_response, jsonify

app = Flask(__name__)


@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/')
@app.route('/invoke')
def basic_pages(**kwargs):
    return make_response(open('static/index.html').read())


@app.route('/api/')
def api():
    return jsonify(first='Foo', last='Bar')

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)