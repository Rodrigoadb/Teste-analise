from flask import Flask, request
from locust import HttpUser, TaskSet, task
import requests
from random import randint
from Calculadora import Calculadora

app = Flask(__name__)




@app.route("/somar", methods=["POST"])
def somar():
    calculadora = Calculadora()
    a = request.json["a"]
    b = request.json["b"]
    return {"soma": calculadora.add(a, b)}


@app.route("/subtrair", methods=["POST"])
def subtrair():
    calculadora = Calculadora()
    a = request.json["a"]
    b = request.json["b"]
    return {"subtracao": calculadora.diminuir(a, b)}


@app.route("/multiplicar", methods=["POST"])
def multiplicar():
    calculadora = Calculadora()
    a = request.json["a"]
    b = request.json["b"]
    return {"multiplicacao": calculadora.mult(a, b)}



@app.route("/dividir", methods=["POST"])
def dividir():
    calculadora = Calculadora()
    a = request.json["a"]
    b = request.json["b"]
    return {"divisao": calculadora.div(a, b)}



@app.route("/potencia", methods=["POST"])
def pot():
    calculadora = Calculadora()
    base = request.json["a"]
    expoente = request.json["b"]
    return {"potencia": calculadora.pot(base, expoente)}



@app.route("/raiz", methods=["POST"])
def radiciacao():
    calculadora = Calculadora()
    radicando = request.json["a"]
    indice = request.json["b"]
    
    return {"raiz": calculadora.rad(radicando, indice)}


if __name__ == "__main__":
    app.run(debug=True)
    a = randint(-15, 15)
