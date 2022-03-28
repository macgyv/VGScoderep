from app import app
from flask import render_template, request, jsonify
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form['message']
    return render_template('message.html', message=message)


@app.route("/forward", methods=['POST'])
def forward():
    message = request.form['message']

    os.environ['HTTP_PROXY'] = 'http://USrD8iSwgj98rX49amoGYiqk:500edfdf-0831-4105-a512-a7d3fd1e9c9d@tnte6doqz8w.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'message': message},
                        verify='{certs/sandbox.pem}')

    res = res.json()
    return render_template('forward.html', response=res)
