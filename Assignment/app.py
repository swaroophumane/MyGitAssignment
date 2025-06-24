from flask import Flask 
import json

app = Flask (__name__)

@app.route('/api') 
def get_data(): 
    data = [
        {'id': 1, 'name': 'Apple'}, 
        {'id': 2, 'name': 'Banana'}, 
        {'id': 3, 'name': 'Cherry'}
        ]
    data= json.dumps(data)
    print(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)