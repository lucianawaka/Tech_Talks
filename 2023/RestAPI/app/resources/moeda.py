from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# Moedas
from models.Dolar import Dolar
from models.Euro import Euro
from models.Real import Real


blp = Blueprint("moedas", __name__, description="Operações nas Moedas")

@blp.route("/moedas")
class MoedaAPI(MethodView):
    def get(self):
        moedas = []
        moedas.append(Dolar().to_json())
        moedas.append(Euro().to_json())
        moedas.append(Real().to_json())
        return moedas