from flask import Flask
import os

app = Flask(__name__)

@app.route("/")

def root():
    result = "Hello World"
    return result

if __name__ == "__main__":
    app.run(debug = True, port = 3000)