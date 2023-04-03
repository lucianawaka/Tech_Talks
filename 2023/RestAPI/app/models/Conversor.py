from .Real import Real
from .Dolar import Dolar
from .Euro import Euro

class Conversor:
    def __init__(self):

        # Instancia as moedas
        self.moedas = {
            "Real": Real(),
            "Dolar": Dolar() ,
            "Euro": Euro()
        }
        
    def converte(self, moeda1: str, moeda2: str, valor: float):
        if moeda1 not in self.moedas or moeda2 not in self.moedas:
            return "Não é possível converter as moedas"
        
        moeda1_obj = self.moedas[moeda1]
        moeda2_obj = self.moedas[moeda2]
        
        valor_convertido, simbolo = moeda1_obj.converter_to(moeda2_obj, valor)
        return {"valor":valor_convertido, "simbolo":simbolo}