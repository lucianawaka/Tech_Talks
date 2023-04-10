from unittest import TestCase

from models.Conversor import Conversor

class TestConversor(TestCase):
    

    def test_conversor_BRL_EUR(self):
        conversor = Conversor()
        conversor.converte("BRL", "EUR", 10)
        expected = {"valor":1.81, "simbolo":"€"} # 5.52
        self.assertDictEqual(expected, conversor.converte("BRL", "EUR", 10))
        
    def test_conversor_EUR_BRL(self):
        conversor = Conversor()
        conversor.converte("EUR", "BRL", 10) 
        expected = {"valor":55.20, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("EUR", "BRL", 10))
        
    def test_conversor_BRL_USD(self):
        conversor = Conversor()
        conversor.converte("BRL", "USD", 10) 
        expected = {"valor":1.97, "simbolo":"$"} # 5.07
        self.assertDictEqual(expected, conversor.converte("BRL", "USD", 10))
        
    def test_conversor_USD_BRL(self):
        conversor = Conversor()
        conversor.converte("USD", "BRL", 10)
        expected = {"valor":50.70, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("USD", "BRL", 10))
        
        
    def test_conversor_BRL_BRL(self):
        conversor = Conversor()
        conversor.converte("BRL", "BRL", 10)
        expected = {"valor":10, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("BRL", "BRL", 10))
        
        
    
        
