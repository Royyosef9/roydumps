import os
import redis
from flask import Flask

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

@app.route("/")
def home():
    visits = r.incr("counter")  
    greeting = os.getenv("APP_GREETING", "ברירת מחדל")
    return f"{greeting} — Visit #{visits}"

@app.route("/about")
def about():
    user = os.getenv("USERNAME", "Anonymous")
    return f" This is RoyApp, running for user: {user}"

@app.route("/secret")
def secret():
    api_key = os.getenv("API_KEY", " Not Set")
    return f" Your API Key is: {api_key}"

@app.route("/dev-check")
def dev_check():
    return "בדיקה מהסניף dev!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
