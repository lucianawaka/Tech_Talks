from models.Conversor import Conversor
from flask import Flask, request

app = Flask(__name__)


@app.route('/conversor/<string:moeda1>/<string:moeda2>/<string:valor>')
def get_moeda_convertida(moeda1, moeda2, valor):
    conversor = Conversor()
    try:
        valor_float = float(valor)
    except ValueError:
        return "O valor tem que ser um número real ou inteiro"
    return conversor.converte(moeda1, moeda2, valor_float)