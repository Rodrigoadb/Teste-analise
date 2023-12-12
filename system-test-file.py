from locust import HttpUser, between, task
from random import randint
import json

# pico de usuários: 100
# locust -f system-test-file.py --headless 

# 5 novos usuarios, realizando novas requisições por segundo 
# -u 100 -r 5 
# --users 10 --spawn-rate 1 

class WebsiteUser(HttpUser):
    host="http://127.0.0.1:5000"
    wait_time = between(5, 15)
    
    @task
    def soma(self):
        a = (randint(-50, 50))
        b = (randint(-50, 50))

        response = self.client.post("/somar", json=({
            "a": a,
            "b": b
        }))
        print(f"Soma: {a} + {b} = {response.json()}")


    @task
    def subtracao(self):
        a = (randint(-50, 50))
        b = (randint(-50, 50))

        response = self.client.post("/subtrair", json=({
            "a": a,
            "b": b
        }))
        print(f"Subtração: ({a}) - ({b}) = {response.json()}")


    @task
    def multiplicacao(self):
        a = (randint(-50, 50))
        b = (randint(-50, 50))

        response = self.client.post("/multiplicar", json=({
            "a": a,
            "b": b
        }))
        print(f"Multiplicação: {a} x {b} = {response.json()}")


    @task
    def divisao(self):
        a = (randint(-50, 50))
        b = (randint(-5, 5))

        response = self.client.post("/dividir", json=({
            "a": a,
            "b": b
        }))
        print(f"Divisão: ({a}) - ({b}) = {response.json()}")


    @task
    def potencia(self):
        a = (randint(-15, 15))
        b = (randint(-15, 15))

        response = self.client.post("/potencia", json=({
            "a": a,
            "b": b
        }))
        print(f"Potenciação: ({a})^({b}) = {response.json()}")


    @task
    def radiciacao(self):
        a = (randint(-50, 50))
        b = (randint(2, 5))
        if b == 0:
            b = 1

        response = self.client.post("/raiz", json=({
            "a": a,
            "b": b
        }))
        print(f"Radiciação: A raiz {b}ª de {a} = {response.json()}")
