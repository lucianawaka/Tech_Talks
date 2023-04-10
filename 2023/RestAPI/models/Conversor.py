from .Real import Real
from .Dolar import Dolar
from .Euro import Euro
from flask_smorest import abort
from flask import jsonify


class Conversor:
    def __init__(self):

        # Instancia as moedas
        self.moedas = {
            "Real": Real(),
            "Dolar": Dolar() ,
            "Euro": Euro()
        }
        
    def converte(self, moeda1: str, moeda2: str, valor: float):
        try:
            if moeda1 in self.moedas or moeda2  in self.moedas:
                moeda1_obj = self.moedas[moeda1]
                moeda2_obj = self.moedas[moeda2]
        
                valor_convertido, simbolo = moeda1_obj.converter_to(moeda2_obj, valor)
                return jsonify({"valor":valor_convertido, "simbolo":simbolo})
            
        except KeyError:
            return abort(500, message="Não é possível converter as moedas! Moedas existentes: {}".format(self.moedas.keys()))
