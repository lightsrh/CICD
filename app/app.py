from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get('/city')
def city_get():
    cities = ["Paris", "London", "New York"]  # replace with actual database query

    cities_json = json.dumps(cities)

    return cities_json, 200

@app.route("/_health")
def health_check():
    return "", 204