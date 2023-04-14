from unittest import TestCase

from models.Dolar import Dolar
from models.Euro import Euro
from models.Real import Real

class TestMoeda(TestCase):
    
    def test_get_real(self):
        dolar = Real()
        expected = {'Moeda': "BRL", 'Simbolo': "R$", 'Valor': 1} # 1
        self.assertDictEqual(expected, dolar.to_json())
        
    
    def test_get_dolar(self):
        dolar = Dolar()
        expected = {'Moeda': "USD", 'Simbolo': "$", 'Valor': 4.93} # 4.93
        self.assertDictEqual(expected, dolar.to_json())
        
    
    def test_get_deuro(self):
        dolar = Euro()
        expected = {'Moeda': "EUR", 'Simbolo': "€", 'Valor': 5.45} # 5.45
        self.assertDictEqual(expected, dolar.to_json())
        
        
    
        
