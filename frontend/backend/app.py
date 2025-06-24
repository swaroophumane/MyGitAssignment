import os
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

My_URI = os.getenv('MONGO_URI')

# uri = "mongodb+srv://swaroop:MyBadPassKey@tram.btqn7sb.mongodb.net/?retryWrites=true&w=majority&appName=Tram"
# Create a new client and connect to the server
client = MongoClient(My_URI , server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Creation of Database.               
db = client.test

collections= db['Testing_Flask_Again']

app = Flask(__name__)


@app.route("/api/<name>")
def name(name):
    return f"<h1>The name used here is, {name}</h1>"

@app.route("/add/<a>/<b>")
def add(a,b):
    answer = int(a) + int(b)
    return f"<h1>The addition is, {answer}</h1>"

@app.route("/api")
def name_Age():
    name = request.values.get('name')
    age = int(request.values.get('age'))

    if age > 18:
        return f'<h1>You can enter in the club, {name}</h1>'
    else:
        return f'<h1>Go back home Mr. {name}</h1>'
    # http://127.0.0.1:5000/api?name=Swaroop&age=32


@app.route('/submit', methods = ['POST'])
def submit():
    form_data = dict(request.json)
    collections.insert_one(form_data)
    return f"<h1>{form_data}</h1>"

@app.route("/view")
def view():
    data = collections.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']

    data = {
        'data':data
    }

    return jsonify(data)


if __name__ == '__main__':
    # change the host and port for backend
    app.run(host='0.0.0.0', port=9000, debug=True)