from unittest import TestCase
import sys
import os

path = os.getcwd()

sys.path.insert(0, path)

from models.Conversor import Conversor


class TestMoeda(TestCase):
        
    def test_conversor_real_euro(self):
        conversor = Conversor()
        conversor.converte("Real", "Euro", 10)
        expected = {"valor":55.20, "simbolo":"€"}
        self.assertEqual(expected, conversor.converte("Real", "Euro", 10))
        
    