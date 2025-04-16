from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/health")
def health():
    print("health check called")
    return {"status": "healthy"}, 200
