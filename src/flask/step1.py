#!/usr/bin/env python
# coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, from flask!"

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8899, debug=True)

