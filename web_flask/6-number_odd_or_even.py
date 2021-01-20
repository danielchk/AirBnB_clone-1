#!/usr/bin/python3
"""initializate flask"""
from flask import Flask, render_template
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
    """show Python followed by text replace to or space"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """if int show: "n" is a number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplates(n):
    """if number show template(HTML)"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    """show if odd or even"""
    if n % 2 == 0:
        dig = 'even'
    else:
        dig = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, dig=dig)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
