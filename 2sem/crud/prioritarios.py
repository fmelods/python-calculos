# contatos prioritários
contatos = []

def criar_contato(nome_usual, nome_completo, telefone_fixo, telefone_celular):
    if len(contatos) >= 20:
        print("Limite de contatos atingido!")
    else:
        contato = {
            "nome_usual": nome_usual,
            "nome_completo": nome_completo,
            "telefone_fixo": telefone_fixo,
            "telefone_celular": telefone_celular
        }
        contatos.append(contato)
        print("Contato adicionado com sucesso!")

def listar_contatos():
    if contatos:
        contatos_ordenados = sorted(contatos, key=lambda x: x['nome_usual'])
        for contato in contatos_ordenados:
            print(f"Nome usual: {contato['nome_usual']}, Nome completo: {contato['nome_completo']}, Telefone fixo: {contato['telefone_fixo']}, Telefone celular: {contato['telefone_celular']}")
    else:
        print("Nenhum contato cadastrado.")

def buscar_contato(nome_usual):
    for contato in contatos:
        if contato["nome_usual"] == nome_usual:
            print(f"Nome completo: {contato['nome_completo']}, Telefone fixo: {contato['telefone_fixo']}, Telefone celular: {contato['telefone_celular']}")
            return
    print("Contato não encontrado.")

def atualizar_contato(nome_usual, novo_nome_completo=None, novo_telefone_fixo=None, novo_telefone_celular=None):
    for contato in contatos:
        if contato["nome_usual"] == nome_usual:
            if novo_nome_completo:
                contato['nome_completo'] = novo_nome_completo
            if novo_telefone_fixo:
                contato['telefone_fixo'] = novo_telefone_fixo
            if novo_telefone_celular:
                contato['telefone_celular'] = novo_telefone_celular
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")

def deletar_contato(nome_usual):
    for i, contato in enumerate(contatos):
        if contato["nome_usual"] == nome_usual:
            contatos.pop(i)
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Consultar contato")
        print("3. Listar contatos")
        print("4. Atualizar contato")
        print("5. Remover contato")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_usual = input("Nome usual: ")
            nome_completo = input("Nome completo: ")
            telefone_fixo = input("Telefone fixo: ")
            telefone_celular = input("Telefone celular: ")
            criar_contato(nome_usual, nome_completo, telefone_fixo, telefone_celular)
        elif opcao == '2':
            nome_usual = input("Nome usual: ")
            buscar_contato(nome_usual)
        elif opcao == '3':
            listar_contatos()
        elif opcao == '4':
            nome_usual = input("Nome usual do contato a atualizar: ")
            novo_nome_completo = input("Novo nome completo (deixe em branco para não alterar): ")
            novo_telefone_fixo = input("Novo telefone fixo (deixe em branco para não alterar): ")
            novo_telefone_celular = input("Novo telefone celular (deixe em branco para não alterar): ")
            atualizar_contato(nome_usual, novo_nome_completo, novo_telefone_fixo, novo_telefone_celular)
        elif opcao == '5':
            nome_usual = input("Nome usual do contato a remover: ")
            deletar_contato(nome_usual)
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
