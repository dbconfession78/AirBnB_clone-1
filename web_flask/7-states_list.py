#!/usr/bin/python3
"""
7-states_list - starts a flask application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(exception):
    """  close storage session """
    storage.close()


@app.route('/states_list')
def states_list():
    app.url_map.strict_slashes = False
    states = storage.all('State').values()
    return (render_template('7-states_list.html', states=states))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
