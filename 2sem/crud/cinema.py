# sistema de venda de bilhetes para cinema
import numpy as np

# Definição da matriz de lugares
cinema = np.full((14, 10), '_')  # Preencher com "_" para assentos vazios
poltronas_vendidas = {} 

def display_cinema():
    for i in range(14):
        print(f"Fileira {i+1}: {' '.join(cinema[i])}")

def vender_bilhete(poltrona, tipo_ingresso, idade):
    if poltrona in poltronas_vendidas:
        print("Poltrona já vendida!")
    else:
        fileira, coluna = divmod(poltrona-1, 10)
        cinema[fileira][coluna] = tipo_ingresso
        poltronas_vendidas[poltrona] = [tipo_ingresso, idade]
        print(f"Poltrona {poltrona} vendida com sucesso!")

def calcular_total():
    meia, inteira, menores_12, menores_18, maiores_idade = 0, 0, 0, 0, 0
    valor_total = 0
    
    for _, (tipo, idade) in poltronas_vendidas.items():
        if tipo == 'm':
            meia += 1
            valor_total += 10  # Valor meia entrada
        elif tipo == 'i':
            inteira += 1
            valor_total += 20  # Valor inteira

        if idade < 12:
            menores_12 += 1
        elif idade < 18:
            menores_18 += 1
        else:
            maiores_idade += 1

    imposto = valor_total * 0.15
    print(f"\nRelatório de Vendas:")
    print(f"Total de meias: {meia}")
    print(f"Total de inteiras: {inteira}")
    print(f"Menores de 12 anos: {menores_12}")
    print(f"Menores de 18 anos: {menores_18}")
    print(f"Maiores de idade: {maiores_idade}")
    print(f"Total arrecadado: R$ {valor_total}")
    print(f"Imposto a ser recolhido (15%): R$ {imposto}")

def main():
    while True:
        print("\nMenu:")
        print("1. Exibir plateia")
        print("2. Vender bilhete")
        print("3. Exibir relatório")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            display_cinema()
        elif opcao == '2':
            poltrona = int(input("Informe a poltrona (1-140): "))
            tipo_ingresso = input("Informe o tipo de ingresso ('m' - meia, 'i' - inteira): ")
            idade = int(input("Informe a idade do cliente: "))
            vender_bilhete(poltrona, tipo_ingresso, idade)
        elif opcao == '3':
            calcular_total()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
