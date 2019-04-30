# flask_app.py
import config
import pandas as pd
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

# Set db config
for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)


class Api(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/api", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        api_request = Api(request=request.method, response="Post some JSON data here!")
        db.session.add(api_request)
        db.session.commit()
        return "Post some JSON data here!"

    if request.method == "POST":
        df = request.get_json(force=True)
        api_request = Api(request=request.method, response=str(df))
        db.session.add(api_request)
        db.session.commit()
        return jsonify(df)