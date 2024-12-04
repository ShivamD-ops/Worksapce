from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello"

@app.route("/home")
def home():
    return f"home"

if __name__ == '__main__':
    app.run()