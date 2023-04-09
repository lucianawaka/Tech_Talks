from unittest import TestCase

from models.Conversor import Conversor

class TestMoeda(TestCase):
    

    def test_conversor_real_euro(self):
        conversor = Conversor()
        conversor.converte("Real", "Euro", 10)
        expected = {"valor":1.81, "simbolo":"€"} # 5.52
        self.assertDictEqual(expected, conversor.converte("Real", "Euro", 10))
        
    def test_conversor_euro_real(self):
        conversor = Conversor()
        conversor.converte("Euro", "Real", 10) 
        expected = {"valor":55.20, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("Euro", "Real", 10))
        
    def test_conversor_real_dolar(self):
        conversor = Conversor()
        conversor.converte("Real", "Dolar", 10) 
        expected = {"valor":1.97, "simbolo":"$"} # 5.07
        self.assertDictEqual(expected, conversor.converte("Real", "Dolar", 10))
        
    def test_conversor_dolar_real(self):
        conversor = Conversor()
        conversor.converte("Dolar", "Real", 10)
        expected = {"valor":50.70, "simbolo":"R$"}
        self.assertDictEqual(expected, conversor.converte("Dolar", "Real", 10))
        
    
        
