from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response('Hello Friend!')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
