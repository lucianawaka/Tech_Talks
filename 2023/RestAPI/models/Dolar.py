from .Moeda import Moeda

class Dolar(Moeda):
    def __init__(self):
        super().__init__(nome = "Dolar", simbolo = "$", valor = 5.07)
