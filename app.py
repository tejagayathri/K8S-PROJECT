from flask import Flask,jsonify
import requests
app = Flask(__name__) 

@app.route('/')
def demo():
    return {'name' : 'Teja Venkatesh'}


@app.route('/users') 
def display():
    api_url = 'https://jsonplaceholder.typicode.com/users/1'
    result = requests.get(api_url)
    result.raise_for_status()

    data = result.json() 
    name = data['name'] 
    city = data['address']['city'] 
    return '{} lives in {}'.format(name,city)
    return data
    return jsonify(data)


app.run()