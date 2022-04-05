from flask import Flask, make_response
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        f = open("hello.txt", "r")
        response = make_response(f.read())
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        response = make_response("Unhelpful Error!")

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
