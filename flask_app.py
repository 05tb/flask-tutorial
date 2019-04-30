# flask_app.py
import pandas as pd
from flask import Flask, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello!"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/api")
def data():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    return jsonify(df.to_json())