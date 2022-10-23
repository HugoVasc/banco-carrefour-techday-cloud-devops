#!/bin/python

import json
from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def index():
  if request.method == 'GET':
    print("GET received")
    return ("Data")
  elif request.method == 'POST':
    data = json.loads(request.data)
    id = randint(1,999)
    nome = data.get('nome')
    email = data.get('email')
    comentario = data.get('comentario')
    print("id: " + str(id) + " nome: " + nome + " email: " + email + " comentario: " + comentario)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
  
app.run(host="localhost", port=8085)