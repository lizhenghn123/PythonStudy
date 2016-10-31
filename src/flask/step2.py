#!/usr/bin/env python
# coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, from flask!"

@app.route("/hello")
def hello():
    return "hello, hello!"

@app.route("/peter")
def sayhi_to_peter():
    return "<h1>hello, peter! You are VIP!</h1>"

@app.route("/<user_name>")
def sayhi(user_name):
    return "<h1>hello, %s! This Message from Flask!</h1>" % user_name

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8899, debug=True)

