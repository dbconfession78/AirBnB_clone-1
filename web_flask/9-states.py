#!/usr/bin/python3
"""
9-sates - starts a flask application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def get_states():
    """ displays an html page with states  """
    states = storage.all('State').values()
#    for state in states:
#        for city in state.cities:
#            input(city.name)

# hold onto this. might need it in anothe rproject
# shows cities by state
#    for k, v in states.items():
#        input(v.name)
#    for v in states.values():
#        input('-- {} --'.format(v.name))
#       for city in v.cities:
#          input('\t{}'.format(city.name))

    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id=None):
    """ displays an html page with a single state  """
    states = storage.all('State')
    if id is None:
        return render_template('9-states.html', states=states.values)

    state = ""
    cities = []
    for k in states.keys():
        if id in k:
            state = states.get(k)
            cities = state.cities
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown(self):
    """ closes storage session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
