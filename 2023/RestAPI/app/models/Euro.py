from .Moeda import Moeda

class Euro(Moeda):
    def __init__(self):
        self.nome = "Euro"
        self.simbolo = "€"
        self.valor = 5.52
        
        