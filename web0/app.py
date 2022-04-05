from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    # Render the hello template, setting the backend API URL
    response = make_response(render_template('hello.html', api_url = "http://localhost:8002/"))
    return response
