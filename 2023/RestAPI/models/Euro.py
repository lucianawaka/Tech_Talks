from .Moeda import Moeda

class Euro(Moeda):
    def __init__(self):
        super().__init__(nome = "EUR", simbolo = "€", valor = 5.45)
