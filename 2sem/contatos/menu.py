#### MENU DE CONTATOS
from crud import *

def menu():
    while True:
        print("0 sair")
        print("1 incluir um novo contato")
        print("2 consultar um contato pelo nome usual")
        print("3 ordenar contato por ordem alfabética")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            create()
        elif opcao == '2':
            read()
        elif opcao == '3':
            exibir()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente")

menu()