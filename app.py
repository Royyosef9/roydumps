# app.py
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "roy site"

@app.route("/roy")
def homeroy():
    return " hello from docker container"

@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
