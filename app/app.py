import requests
import re

from datetime import datetime, timedelta
from json import dumps, load, loads

from flask import Flask, render_template, Response, request

from connect_db.connect import mongoDBConnector
def sample_function():
    """This is a sample docstring subject

    This is a sample docstring description.

    Args:
        s (str): a string argument
        i (int): an integer argument

    Returns:
         dict: a dictionary is returned

    Raises:
        Any exception to be caught later.
    """
    return "Hello World"

mongoDB_connector = mongoDBConnector()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Return the index.html page"""
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def api():
    """This is an api endpoint"""
    data = {"Hi there": "This is a sample response"}
    return Response(dumps(data), status=200, mimetype='application/json')


@app.route('/api/<string:variable>', methods=['GET'])
def api_variable(variable):
    """This is an api endpoint with a string variable as url parameter"""
    data = {"You entered variable:": variable}
    return Response(dumps(data), status=200, mimetype='application/json')

@app.route('/music')
def list_musics():
    musics = mongoDB_connector.find_all('music')
    return render_template('musics.html', musiques=musics)

@app.route('/recherche')
def rech_artiste():
    musics = mongoDB_connector.recherche('music', request.args.get("query"))
    return render_template('musics.html', musiques=musics)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
