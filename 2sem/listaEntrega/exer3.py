import json

MAX_CONTACTS = 20
contacts = []

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    if len(contacts) >= MAX_CONTACTS:
        print("Lista de contatos cheia!")
        return
    nome_usual = input("Nome usual: ")
    nome_completo = input("Nome completo: ")
    telefone_fixo = input("Telefone fixo: ")
    telefone_celular = input("Telefone celular: ")
    contacts.append({
        "nome_usual": nome_usual,
        "nome_completo": nome_completo,
        "telefone_fixo": telefone_fixo,
        "telefone_celular": telefone_celular
    })
    save_contacts()

def search_contact():
    nome_usual = input("Nome usual para buscar: ")
    for contact in contacts:
        if contact["nome_usual"] == nome_usual:
            print(f"Nome completo: {contact['nome_completo']}")
            print(f"Telefone fixo: {contact['telefone_fixo']}")
            print(f"Telefone celular: {contact['telefone_celular']}")
            return
    print("Contato inexistente")

def list_contacts():
    sorted_contacts = sorted(contacts, key=lambda x: x["nome_usual"])
    for contact in sorted_contacts:
        print(f"Nome usual: {contact['nome_usual']}")
        print(f"Nome completo: {contact['nome_completo']}")
        print(f"Telefone fixo: {contact['telefone_fixo']}")
        print(f"Telefone celular: {contact['telefone_celular']}")
        print("")

def main():
    global contacts
    contacts = load_contacts()
    while True:
        print("Menu:")
        print("0 - Sair")
        print("1 - Incluir um novo contato")
        print("2 - Consultar um contato")
        print("3 - Exibir listagem de contatos")
        option = input("Escolha uma opção: ")
        if option == "0":
            break
        elif option == "1":
            add_contact()
        elif option == "2":
            search_contact()
        elif option == "3":
            list_contacts()
        else:
            print("Opção inválida")



main()