class Moeda:
    
    def __init__(self, nome, simbolo, valor):
        self.nome = nome
        self.simbolo = simbolo
        self.valor = valor
        
    def __str__(self):
        return 'Moeda: {}, Simbolo: {}, Valor: {}'.format(self.nome, self.simbolo, self.valor)