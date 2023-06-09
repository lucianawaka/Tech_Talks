from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from schemas import ConversorSchema
from flask import jsonify

# Conversor
from models.Conversor import Conversor

blp = Blueprint("Conversor", __name__, description="Operações para Conversão de Moedas")
    
@blp.route('/conversor/<string:moeda1>/<string:moeda2>/<string:valor>')
class ConversorAPI(MethodView):
    @jwt_required()
    
    @blp.response(200, ConversorSchema)
    def get(self, moeda1, moeda2, valor):
        conversor = Conversor()
        try:
            valor_float = float(valor)
        except ValueError:
            abort(406, message="O valor tem que ser um número real ou inteiro")
        return jsonify(conversor.converte(moeda1, moeda2, valor_float))
