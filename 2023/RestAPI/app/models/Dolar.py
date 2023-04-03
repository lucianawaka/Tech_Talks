from .Moeda import Moeda

class Dolar(Moeda):
    def __init__(self):
        self.nome = "Dolar"
        self.simbolo = "$"
        self.valor = 5.07
