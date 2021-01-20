#!/usr/bin/python3
"""initializate flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """show Hello HBNB!"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def functionc(text):
    """show C followed by text replace to _ or space"""
    return ('C ' + text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def functionp(text='is cool'):
    """show Python followed by text replace to _ or space"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
