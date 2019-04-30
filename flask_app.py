# flask_app.py
import pandas as pd
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello!"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/api", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return "Post some JSON data here!"

    if request.method == "POST":
        df = request.get_json(force=True)
        return jsonify(df)