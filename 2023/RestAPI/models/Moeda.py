class Moeda:
    
    def __init__(self, nome: str, simbolo: str, valor: float):
        self.nome = nome
        self.simbolo = simbolo
        self.valor = valor
    
    def __str__(self):
        return 'Moeda: {}, Simbolo: {}, Valor: {}'.format(self.nome, self.simbolo, self.valor)
    
    def to_json(self):
        return {
            'Moeda': self.nome,
            'Simbolo': self.simbolo,
            'Valor': self.valor,
        }