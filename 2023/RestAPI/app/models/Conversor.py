from .Real import Real
from .Dolar import Dolar
from .Euro import Euro

class Conversor:
    def __init__(self, moeda1: str, moeda2: str, valor: float):
        self.moeda1 = moeda1
        self.moeda2 = moeda2
        self.valor = valor
        
    def converte(self):
        real = Real()
        dolar = Dolar()
        euro = Euro()
        
        if self.moeda1 == real.nome and self.moeda2 == dolar.nome:
            return {"valor":self.valor / dolar.valor, "simbolo": dolar.simbolo} 
        elif self.moeda1 == dolar.nome and self.moeda2 == real.nome:
            return {"valor":self.valor * dolar.valor, "simbolo": real.simbolo} 
        elif self.moeda1 == real.nome and self.moeda2 == euro.nome:
            return {"valor":self.valor / euro.valor, "simbolo": euro.simbolo} 
        elif self.moeda1 == euro.nome and self.moeda2 == real.nome:
            return {"valor":self.valor * euro.valor, "simbolo": real.simbolo} 
        else: 
            return "Não foi possível coverter a moeda {} para {}".format(self.moeda1, self.moeda2)