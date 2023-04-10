from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from schemas import MoedaShema
from flask import jsonify

# Moedas
from models.Dolar import Dolar
from models.Euro import Euro
from models.Real import Real


blp = Blueprint("Moedas", __name__, description="Operações nas Moedas")

@blp.route("/moedas")
class MoedaAPI(MethodView):
    @jwt_required()
    @blp.response(200, MoedaShema(many=True))
    def get(self):
        moedas = []
        moedas.append(Dolar().to_json())
        moedas.append(Euro().to_json())
        moedas.append(Real().to_json())
        return jsonify(moedas)