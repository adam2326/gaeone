
import logging

from flask import Flask
import datetime


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Adams World: ' + str(datetime.datetime.now())


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
