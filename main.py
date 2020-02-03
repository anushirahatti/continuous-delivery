#push
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<h1>Hello Aniruddha!</h1>'

@app.route('/deliver')
def hey():
    """Return a friendly HTTP greeting."""
    return '<h1>Continuous Delivery on GCP Success!</h1>'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
