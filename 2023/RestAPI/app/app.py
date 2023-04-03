from models.Conversor import Conversor


def main():
    conversor = Conversor()
    print(conversor.converte("Euro","Real", 100))
    
if __name__== "__main__":
    main()