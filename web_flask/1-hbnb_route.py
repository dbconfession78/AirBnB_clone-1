#!/usr/bin/python3
"""
1-hbnb_route.py - starts a Flask web application
"""
from flask import Flask
app = Flask('__name__')


@app.route('/')
def hello_hbnb():
    """ outputs 'Hello HBNB!' """
    app.url_map.strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ outputs 'HBNB' """
    app.url_map.strict_slashes = False
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
