from .Moeda import Moeda

class Real(Moeda):
    def __init__(self):
        self.nome = "Real"
        self.simbolo = "R$"
        self.valor = 1
