from models.Conversor import Conversor

def main():
    conversor = Conversor("Dolar","Real", 2)
    print(conversor.converte())
    
if __name__== "__main__":
    main()