from .Moeda import Moeda

class Euro(Moeda):
    def __init__(self):
        super().__init__(nome = "Euro", simbolo = "€", valor = 5.52)
