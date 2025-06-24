import os
from flask import Flask, render_template, request
from datetime import datetime

import requests

BACKEND_URL = 'http://127.0.0.1:9000'

app = Flask(__name__)

@app.route("/")
def hello_world():
    dayOfWeek = datetime.now().strftime('%A')
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', dayOfWeek = dayOfWeek,current_time=current_time )

@app.route("/second")
def second():
    return "<h1>This is Second Page</h1>"

@app.route('/submit', methods = ['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return "Data Submitted Successfully"

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/view')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)