import json
def main(args =[]):
    while true:
        try:
            f = open("meses.txt", )
            linhas = f.readlins()

            for linha in linhas:
            print(linha.strip())

            break
        except FileNotFoundError :
        print("Arquivo não encontrado!")
