from urllib import response
import flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('./get_location_names')

def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
        })
    response.headers.add('Acess-control-Allow-Origin, ')
    return response


if __name__=="__main__":
    print("Starting flask server..")
    app.run() 