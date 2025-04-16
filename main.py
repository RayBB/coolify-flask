from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello world called")
    return "<p>Hello, World!</p>"

@app.route('/health', methods=['GET']) 
def health(): 
    print("health check called")
    return  {"status":"healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
