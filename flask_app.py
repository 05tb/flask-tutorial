# flask_app.py
import config
import pickle
import pandas as pd
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer

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
    route = db.Column(db.Text, nullable=False)
    method = db.Column(db.Text, nullable=False)
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
        api_request = Api(route="/api",
                          method=request.method,
                          request=request.method,
                          response="Post some JSON data here!")
        db.session.add(api_request)
        db.session.commit()
        return "Post some JSON data here!"

    if request.method == "POST":
        df = request.get_json(force=True)
        api_request = Api(route="/api",
                          method=request.method,
                          request=str(request.get_json(force=True)),
                          response=str(df))
        db.session.add(api_request)
        db.session.commit()
        return jsonify(df)


@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.get_json(force=True)
    user_input = list(user_input)
    print(user_input)

    model = pickle.load(open("model.pickle", "rb"))
    vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

    X_user = pd.DataFrame(vectorizer.transform(user_input).toarray(),
                          columns=vectorizer.get_feature_names())

    prediction = model.predict(X_user)
    prediction = prediction.tolist()

    api_request = Api(route="/predict",
                      method=request.method,
                      request=str(user_input),
                      response=str(prediction))
    db.session.add(api_request)
    db.session.commit()

    return jsonify(prediction)


# @app.route("/train", methods=["POST"])
# def train():
#     return 
