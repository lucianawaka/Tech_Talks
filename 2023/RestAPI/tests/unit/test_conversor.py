from unittest import TestCase

from models.Conversor import Conversor

class TestConversor(TestCase):
    

    def test_conversor_BRL_EUR(self):
        conversor = Conversor()
        conversor.converte("BRL", "EUR", 10)
        expected = {"valor":1.83, "simbolo":"€"} # 5.45
        self.assertDictEqual(expected, conversor.converte("BRL", "EUR", 10))
        
    def test_conversor_EUR_BRL(self):
        conversor = Conversor()
        conversor.converte("EUR", "BRL", 10) 
        expected = {"valor":54.50, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("EUR", "BRL", 10))
        
    def test_conversor_BRL_USD(self):
        conversor = Conversor()
        conversor.converte("BRL", "USD", 10) 
        expected = {"valor":2.03, "simbolo":"$"} # 4.93
        self.assertDictEqual(expected, conversor.converte("BRL", "USD", 10))
        
    def test_conversor_USD_BRL(self):
        conversor = Conversor()
        conversor.converte("USD", "BRL", 10)
        expected = {"valor":49.30, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("USD", "BRL", 10))
        
        
    def test_conversor_BRL_BRL(self):
        conversor = Conversor()
        conversor.converte("BRL", "BRL", 10)
        expected = {"valor":10, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("BRL", "BRL", 10))
        
        
    
        
