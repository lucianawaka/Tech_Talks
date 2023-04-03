class Moeda:
    
    def __init__(self, nome: str, simbolo: str, valor: float):
        self.nome = nome
        self.simbolo = simbolo
        self.valor = valor
        
    def converter_to(self, moeda, valor):
        if moeda.nome == self.nome:
            return valor
        converted_value = valor * self.valor / moeda.valor
        return round(converted_value, 2), moeda.simbolo
    
    def __str__(self):
        return 'Moeda: {}, Simbolo: {}, Valor: {}'.format(self.nome, self.simbolo, self.valor)