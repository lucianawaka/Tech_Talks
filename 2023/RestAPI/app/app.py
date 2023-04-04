from models.Conversor import Conversor
from models.Dolar import Dolar
from models.Euro import Euro
from models.Real import Real

from flask import Flask

app = Flask(__name__)


@app.route('/conversor/<string:moeda1>/<string:moeda2>/<string:valor>')
def get_moeda_convertida(moeda1, moeda2, valor):
    conversor = Conversor()
    try:
        valor_float = float(valor)
    except ValueError:
        return "O valor tem que ser um número real ou inteiro"
    return conversor.converte(moeda1, moeda2, valor_float)

@app.get('/moedas')
def get_todas_moedas():
    moedas = []
    moedas.append(Dolar().to_json())
    moedas.append(Euro().to_json())
    moedas.append(Real().to_json())
    return moedas
    