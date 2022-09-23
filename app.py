import os
from flask import Flask, abort, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException

from helpers import Detecting_change, Season, Order_status

# Web app
app = Flask(__name__)

# Pagina principal
@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")

# Path Exercise 1
@app.route("/detecting_change", methods=["POST"])
def exercise1():
    """Handle requests for /score via POST"""

    # Saving the CSV file
    uploaded_file = request.files['filename']
    if not uploaded_file.filename:
        abort(400, "missing file")

    filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
    uploaded_file.save(filepath)

    # Tabulation
    dict = Detecting_change(filepath)

    if not dict:
        abort(422, "Wrong CSV file")

    # Output rendering
    return render_template("table.html", dict=dict, title='Date', data='Was Rainy', func='Detecting change')

# Path exercise 2
@app.route("/seasons", methods=["POST"])
def exercise2():
    """Handle requests for /score via POST"""

    # Saving the CSV file
    uploaded_file = request.files['filename']
    if not uploaded_file.filename:
        abort(400, "missing file")

    filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
    uploaded_file.save(filepath)

    # Tabulation
    dict = Season(filepath)

    if not dict:
        abort(422, "Wrong CSV file")

    # Output rendering
    return render_template("table.html", dict=dict, title='Ord_id', data='Season', func='Seasons')


# Path Exercise3
@app.route("/order_status", methods=["POST"])
def exercise3():
    """Handle requests for /score via POST"""

    # Saving the CSV file
    uploaded_file = request.files['filename']
    if not uploaded_file.filename:
        abort(400, "missing file")

    filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
    uploaded_file.save(filepath)

    # Tabulation
    dict = Order_status(filepath)

    if not dict:
        abort(422, "Wrong CSV file")

    # Output rendering
    return render_template("table.html", dict=dict, title='Order Number', data='Status', func='Order Status')



# En caso de error
@app.errorhandler(HTTPException)
def errorhandler(error):
    """Handle errors"""
    return render_template("error.html", error=error), error.code


# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

app.config['FILE_UPLOADS'] = "./FILE_UPLOADS/"