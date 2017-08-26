import json
def main(args =[]):
    while True:
        try:
            f = open("meses.txt", encoding="utf8")
            linhas = f.readlines()
            
            for linha in linhas:
                print(linha.strip())

            break
            
        except FileNotFoundError :
            print("Arquivo não encontrado!")
            
        finally:
            print('Imprima essa mensagem de qualquer forma (testando o finally)')

if __name__ == '__main__':
    main()
