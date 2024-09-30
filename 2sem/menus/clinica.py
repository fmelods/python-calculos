# menu de clínica veterinária
import time
from collections import deque

pets = []
veterinarios = []
procedimentos = []
fila_pets = deque()
pets_atendidos = []

def cadastrar_pet():
    codigo = len(pets) + 1
    nome_animal = input("Nome do Animal: ")
    tipo_animal = input("Tipo de Animal: ")
    nome_tutor = input("Nome do Tutor: ")
    endereco_tutor = input("Endereço do Tutor: ")
    sintoma = input("Sintoma: ")
    data_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    pet = {'codigo': codigo, 'nome_animal': nome_animal, 'tipo_animal': tipo_animal, 
           'nome_tutor': nome_tutor, 'endereco_tutor': endereco_tutor, 'sintoma': sintoma, 
           'data_hora': data_hora}
    pets.append(pet)
    fila_pets.append(pet)
    print(f"{nome_animal} cadastrado e enfileirado!")

def cadastrar_veterinario():
    codigo = len(veterinarios) + 1
    nome = input("Nome do Veterinário: ")
    endereco = input("Endereço: ")
    email = input("E-mail: ")
    veterinario = {'codigo': codigo, 'nome': nome, 'endereco': endereco, 'email': email}
    veterinarios.append(veterinario)
    print(f"Veterinário {nome} cadastrado!")

def cadastrar_procedimento():
    descricao = input("Descrição do Procedimento: ")
    valor = float(input("Valor do Procedimento: "))
    procedimentos.append({'descricao': descricao, 'valor': valor})
    print(f"Procedimento '{descricao}' cadastrado!")

def atender_pet():
    if not fila_pets:
        print("Nenhum pet na fila.")
        return

    pet = fila_pets.popleft()
    print(f"Atendendo {pet['nome_animal']}...")

    print("Veterinários disponíveis:")
    for vet in veterinarios:
        print(f"{vet['codigo']} - {vet['nome']}")
    
    vet_id = int(input("Escolha o veterinário pelo código: "))
    veterinario = next((vet for vet in veterinarios if vet['codigo'] == vet_id), None)

    if veterinario:
        print("Procedimentos disponíveis:")
        for i, proc in enumerate(procedimentos):
            print(f"{i + 1} - {proc['descricao']} ({proc['valor']})")

        proc_id = int(input("Escolha o procedimento: ")) - 1
        procedimento = procedimentos[proc_id]
        data_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pet_atendido = {'pet': pet, 'veterinario': veterinario, 'procedimento': procedimento, 'data_hora': data_hora}
        pets_atendidos.append(pet_atendido)
        print(f"Pet {pet['nome_animal']} atendido por {veterinario['nome']} no procedimento {procedimento['descricao']}.")

def exibir_relatorio():
    print("\nRelatório de Pets Atendidos")
    total_recebido = 0
    for item in pets_atendidos:
        print(f"Pet: {item['pet']['nome_animal']}, Veterinário: {item['veterinario']['nome']}, Procedimento: {item['procedimento']['descricao']}, Data/Hora: {item['data_hora']}")
        total_recebido += item['procedimento']['valor']

    lucro = total_recebido * 0.35
    print(f"Total Recebido: {total_recebido}")
    print(f"Lucro (35%): {lucro:.2f}")

# Menu principal
while True:
    print("\n1 - Cadastrar Pet")
    print("2 - Cadastrar Veterinário")
    print("3 - Cadastrar Procedimento")
    print("4 - Atender Pet")
    print("5 - Exibir Relatório")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_pet()
    elif opcao == '2':
        cadastrar_veterinario()
    elif opcao == '3':
        cadastrar_procedimento()
    elif opcao == '4':
        atender_pet()
    elif opcao == '5':
        exibir_relatorio()
    elif opcao == '0':
        break
    else:
        print("Opção inválida!")
