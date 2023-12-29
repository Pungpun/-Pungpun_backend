from flask import Flask,request
from dotenv import load_dotenv
import os
import requests
import json

# load .env
load_dotenv()

KEY = os.environ.get('KEY')

app = Flask(__name__)

@app.route("/api")
def api():
    country = request.args.get("country")
    req = requests.get(url=f"https://api.weatherapi.com/v1/current.json?key={KEY}&q=Seoul")
    jsonObj = json.loads(req.text)
    dictionary = {
        "country" : jsonObj["location"]["country"],
        "temp_c" : jsonObj["current"]["temp_c"],
        "condition" : jsonObj["current"]["condition"]["text"],
        "humidity" : jsonObj["current"]["humidity"]
    }
    return dictionary

if __name__ == '__main__':
    app.run(port=3000,debug=True)
