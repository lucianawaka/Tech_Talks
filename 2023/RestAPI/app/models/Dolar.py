from Moeda import Moeda

class Dolar(Moeda):
    def __init__(self):
        self.nome = "Dolar"
        self.simbolo = "$"
        self.valor = 5.07
        super.__init__(nome=self.nome, simbolo=self.simbolo, valor=self.valor)