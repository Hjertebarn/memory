import os
import re
import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, make_response
from flask_session import Session
import json

from cs50 import SQL
from helpers import createTable, apiKeys


# Configure application
app = Flask(__name__)
APPLICATION_SETTINGS = "settings.cfg"
if os.path.exists(APPLICATION_SETTINGS):
    app.config.from_pyfile('settings.cfg')

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memory.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/two", methods=["GET", "POST"])
def two():
    """Creates a 2x4 Memory Table."""
    table = createTable(4)
    return render_template("two.html", table=table)


@app.route("/three", methods=["GET", "POST"])
def three():
    """Creates a 3x4 Memory Table."""
    table = createTable(6)
    return render_template("three.html", table=table)


@app.route("/four", methods=["GET", "POST"])
def four():
    """Creates a 4x4 Memory Table."""
    table = createTable(8)
    return render_template("four.html", table=table)


@app.route('/won', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        attempts = request.form['attempts']
        time = request.form['time']
        grid = request.form['grid']

        rows = db.execute("SELECT * FROM ranking{0} ORDER BY time, attempts ASC".format(grid))

        resp = make_response(render_template('won.html', attempts=attempts, time=time, rows=rows))
        resp.set_cookie('attempts', attempts)
        resp.set_cookie('time', time)
        resp.set_cookie('grid', grid)
        return resp


@app.route("/ranking", methods=["GET", "POST"])
def ranking():
    """Shows ranking page"""
    attempts = request.cookies.get('attempts')
    time = request.cookies.get('time')
    grid = request.cookies.get('grid')
    print("grid: " + grid)

    if request.method == "POST":
        db.execute("INSERT INTO ranking{0} (name, time, attempts) VALUES (:name, :time, :attempts)".format(grid),
                    name=request.form.get("name"), time=time, attempts=attempts)
    rows = db.execute("SELECT * FROM ranking{0} ORDER BY time, attempts ASC".format(grid))
    return render_template("ranking.html", rows=rows, grid=grid)



