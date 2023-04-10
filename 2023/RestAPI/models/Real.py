from .Moeda import Moeda

class Real(Moeda):
    def __init__(self):
        super().__init__(nome = "BRL", simbolo = "R$", valor = 1)