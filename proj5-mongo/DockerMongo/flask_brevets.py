"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import os
import flask
from flask import request, redirect, url_for, render_template
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
from pymongo import MongoClient
import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.timedb
db.timedb.delete_many({})
###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")

    km = request.args.get('km', type=float)
    brevet = request.args.get('brevet', type=str)
    brevet = int(brevet[:-2])
    date = request.args.get('date', type=str)
    time = request.args.get('time', type=str)
    date_t = date + ' ' + time + ':00'
    app.logger.debug("time man ={}".format(date_t))
    arrow_time = arrow.get(date_t, 'YYYY-MM-DD HH:mm:ss')

    app.logger.debug("brevet={}".format(brevet))
    app.logger.debug("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, brevet, arrow_time.isoformat())
    close_time = acp_times.close_time(km, brevet, arrow_time.isoformat())
    result = {"open": open_time, "close": close_time }
    return flask.jsonify(result=result)

@app.route("/submit", methods=['POST'])
def submit():
    if(db.timedb.find() == None):
        return flask.redirect()
    db.timedb.delete_many({})
    time = request.get_data()
    app.logger.debug('wtf={}'.format(time))
    badrepresentation = {
        '_id': 'time',
        'ciphered': time
    }
    db.timedb.insert_one(badrepresentation)
    return flask.make_response('', 200)
@app.route("/display", methods=['POST'])
def display():
    times1 = db.timedb.find()
    times = [time for time in times1]

    return render_template('display.html', times=times)
    

#############

app.debug = True
app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
