import requests
from flask import render_template
from app import app

@app.route("/")
def index():
    temp = requests.get("http://192.168.0.87").text.split("temp")[1][1:5]
    return render_template("index.html", temp=temp)

@app.route("/temp")
def temp():
    temp = requests.get("http://192.168.0.87").text.split("temp")[1][1:5]
    return temp
