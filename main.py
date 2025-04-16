from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello world called")
    return "<p>Hello, World!</p>"

@app.route('/health', methods=['GET']) 
def health(): 
    return  {"status":"healthy"}, 200
