import time
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "PONG"


@app.route("/fetch/<site>")
def fetch(site):
    print("Fetching", site)
    time.sleep(2)
    return requests.get("https://" + site).text


@app.route("/exit")
def exit():
    request.environ.get("werkzeug.server.shutdown")()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
