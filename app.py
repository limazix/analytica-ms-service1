from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Service 1"

@app.route("/hello/<username>")
def hello(username):
    return "Hello {} from Service 1".format(
        'world' if username in None else username
    )
