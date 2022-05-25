import requests
from flask import Flask

app = Flask(__name__) #cria o site
faturamento = 'teste'

#a api sempre será construída com essas duas funcionalidades:
@app.route("/") #decorator -> diz em qual link a função vai rodar
def hello_world(): #function
    return f"<p style='font-size: 80px'>Hello, World! {faturamento}</p>"

@app.route("/teste")
def teste():
    return "<p>teste</p>"

## como estamos construindo uma REST API, a intenção é que a requisição retorne um json e não um html:
@app.route("/dicionario")
def dicionario(): #function
    return {
        "teste": "1",
        "teste2": "2"
    }

app.run() #coloca o site no ar