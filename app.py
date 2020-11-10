from flask import Flask, request, Response
import mariadb
import json

app = Flask(__name__)
animals = ["Giraffe", "Dog", "Cat", "Ferret", "Cow", "Horse", "Pig", "Lion", "Snake", "Lizard"]

# @app.route('/')
# def homepage():
#     return "Hello World"

# GET, POST, PATCH, DELETE Requests:
@app.route('/animals', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def animals():
    if request.method == 'GET':
        return Response(JSON.dumps(animals, default = str), mimetype = "application/json", status=200)
    elif request.method == 'POST':
        return Response("Successfully added 'Penguin'!", mimetype = "text/html", status = 201)
    elif request.method == 'PATCH':
        return Response("Successfully changed 'Penguin' to 'Seal'. ", mimetype = "text/html", status = 201)
    elif request.method == 'DELETE':
        return Response("Successfully deleted Cow! ", mimetype = "text/html", status = 201)
    else:
        return Response("Uh oh, an error occurred! ", mimetype = "text/html", status = 401)
        
        