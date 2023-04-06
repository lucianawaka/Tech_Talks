from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ConversorSchema

# Conversor
from models.Conversor import Conversor

blp = Blueprint("conversor", __name__, description="Operações para Conversão de Moedas")
    
@blp.route('/conversor/<string:moeda1>/<string:moeda2>/<string:valor>')
class ConversorAPI(MethodView):
    @blp.response(200, ConversorSchema)
    def get(self, moeda1, moeda2, valor):
        conversor = Conversor()
        try:
            valor_float = float(valor)
        except ValueError:
            abort(406, message="O valor tem que ser um número real ou inteiro")
        return conversor.converte(moeda1, moeda2, valor_float)     
