from models.Conversor import Conversor
from flask import Flask

app = Flask(__name__)

@app.get("/conversor")
def get_moeda_convertida():
    conversor = Conversor()
    return conversor.converte("Euro","Real", 100)