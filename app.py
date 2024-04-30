from flask import Flask
import json
import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    load_dotenv()
    app.run(host=os.getenv("CITY_API_ADDR"), port=os.getenv("CITY_API_PORT"), debug=True)