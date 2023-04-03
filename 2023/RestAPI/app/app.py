from models.Conversor import Conversor


def main():
    conversor = Conversor()
    print(conversor.converte("Euro","Euro", 100))
    
if __name__== "__main__":
    main()