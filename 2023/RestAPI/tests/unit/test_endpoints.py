from unittest import TestCase
import requests
# Moedas
from models.Dolar import Dolar
from models.Euro import Euro
from models.Real import Real

# Conversor
import requests
import json

class TestEndpoint(TestCase):
    URL = "https://conversor-api.onrender.com/"
    data = {
        "username":"luciana",
        "password":"12345"
    }
    
    # Somente uma vez
    # def test_endpoint_register(self):

    #     user_payload = json.dumps({
    #         "username": self.data['username'],
    #         "password": self.data['password']
    #     })
    #     resp = requests.post(self.URL+'/register', headers={"Content-Type": "application/json"}, data=user_payload)
    #     self.assertEqual(200, resp.status_code)
        
        
    def test_endpoint_moedas(self):
        
        # Login first 
        user_payload = json.dumps({
            "username": self.data['username'],
            "password": self.data['password']
        })
        response = requests.post(self.URL+'/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json()['access_token']
        # Token
        resp = requests.get(self.URL+'/moedas', headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})
        moedas = []
        moedas.append(Dolar().to_json())
        moedas.append(Euro().to_json())
        moedas.append(Real().to_json())
        self.assertEqual(moedas, resp.json())
        self.assertEqual(200, resp.status_code)

        
    
    def test_endpoint_conversor(self):
                
        # Login first 
        user_payload = json.dumps({
            "username": self.data['username'],
            "password": self.data['password']
        })
        response = requests.post(self.URL+'/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json()['access_token']
        # Token
        moeda1 = 'BRL'
        moeda2 = 'USD'
        valor = '10'
        resp = requests.get(self.URL+'/conversor/'+moeda1+'/'+moeda2+'/'+valor, headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        self.assertEqual(resp.json()['simbolo'], "$")
        self.assertEqual(resp.json()['valor'], 1.83)
        self.assertEqual(200, response.status_code)
        
   

        
