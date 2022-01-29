#!/usr/bin/python3
'''
Write a script that starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/(<text>): display “Python ”,
        The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''display “Hello HBNB!” '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''display “HBNB” '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    '''display “C is ...” '''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text="is cool"):
    '''display “Python is ...” '''
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number_template/<int:n>/", strict_slashes=False)
def html_integer(n):
    '''
    display a HTML page only if n is an integer
    '''
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
