from .Moeda import Moeda

class Real(Moeda):
    def __init__(self):
        super().__init__(nome = "Real", simbolo = "R$", valor = 1)