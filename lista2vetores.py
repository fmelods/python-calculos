# 1 - verificar se a segunda string ocorre dentro da primeira
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

posicao = string1.find(string2)

if posicao != -1:
    print(f"{string2} encontrado na posição {posicao} de {string1}.")
else:
    print(f"{string2} não foi encontrado em {string1}.")

# 2 - gerar uma terceira string com os caracteres em comum
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
comuns = ''.join(sorted(set(string1) & set(string2)))
print(f"Caracteres comuns: {comuns}")

# 3 - gerar terceira lista sem elementos repetidos
lista1 = input("Digite a primeira lista de números separados por espaço: ").split()
lista2 = input("Digite a segunda lista de números separados por espaço: ").split()
lista_unica = list(set(lista1 + lista2))
print(f"Lista combinada sem repetição: {lista_unica}")

# 4 - forma correta de chamar o pop em uma lista
lista_vazia = []
if lista_vazia:
    lista_vazia.pop()
else:
    print("A lista está vazia, não é possível remover elementos.")

# 5 - comparar duas listas usando operações com conjuntos
lista1 = input("Digite a primeira lista de números separados por espaço: ").split()
lista2 = input("Digite a segunda lista de números separados por espaço: ").split()
set1 = set(lista1)
set2 = set(lista2)

# Valores comuns às duas listas
comuns = set1 & set2
print(f"Valores comuns: {comuns}")

# Valores que só existem na primeira lista
somente_primeira = set1 - set2
print(f"Valores só na primeira lista: {somente_primeira}")

# Valores que só existem na segunda lista
somente_segunda = set2 - set1
print(f"Valores só na segunda lista: {somente_segunda}")

# Lista com elementos não repetidos das duas listas
nao_repetidos = set1 ^ set2
print(f"Elementos não repetidos: {nao_repetidos}")

# Primeira lista sem os elementos repetidos da segunda
primeira_sem_repetidos = set1 - comuns
print(f"Primeira lista sem os repetidos da segunda: {primeira_sem_repetidos}")

# 6 - verificar se um número é palíndromo
numero = input("Digite um número: ")
if numero == numero[::-1]:
    print(f"{numero} é um número palíndromo.")
else:
    print(f"{numero} não é um número palíndromo.")

# 7 - sistema de hospital com menu
import time

fila = []
pacientes_atendidos = []

def enfileirar():
    paciente = input("Digite a área do paciente (G, O, C, P, F): ").upper()
    fila.append(paciente)
    print(f"Paciente da área {paciente} adicionado à fila.")

def cadastrar():
    if fila:
        paciente = fila.pop(0)
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        carteirinha = input("Carteirinha: ")
        sintomas = input("Descrição dos sintomas (duas palavras): ")
        area = paciente
        data_hora = time.strftime("%d/%m/%Y %H:%M:%S")

        cadastro = {
            'Nome': nome,
            'Endereço': endereco,
            'Carteirinha': carteirinha,
            'Área de atendimento': area,
            'Data e Hora': data_hora,
            'Sintomas': sintomas
        }

        pacientes_atendidos.append(cadastro)
        print("Paciente cadastrado com sucesso.")
    else:
        print("Nenhum paciente na fila.")

def relatorio():
    if pacientes_atendidos:
        print("Relatório de pacientes atendidos:")
        for paciente in pacientes_atendidos:
            print(paciente)
    else:
        print("Nenhum paciente atendido ainda.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Enfileirar paciente")
    print("2. Cadastrar paciente")
    print("3. Exibir relatório de pacientes atendidos")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        enfileirar()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        relatorio()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")