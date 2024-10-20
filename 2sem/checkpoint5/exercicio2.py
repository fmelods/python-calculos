# Salvado em JSON
import json
from datetime import datetime

produtos = []

# Create
def incluir_produto(codigo, nome, tipo, data_entrada, quantidade, valor_entrada):
    produto = {
        "Codigo": codigo,
        "Nome": nome,
        "Tipo": tipo,
        "Data de Entrada": data_entrada,
        "Quantidade": quantidade,
        "Valor de Entrada": valor_entrada,
        "Valor de Venda Sugerido": valor_entrada * 1.35  # 35% a mais que o valor de entrada
    }
    produtos.append(produto)
    print(f"Produto {nome} incluído com sucesso.")

# Update
def atualizar_produto(codigo, nome="", tipo="", data_entrada="", quantidade="", valor_entrada=""):
    for produto in produtos:
        if produto["Codigo"] == codigo:
            if nome:
                produto["Nome"] = nome
            if tipo:
                produto["Tipo"] = tipo
            if data_entrada:
                produto["Data de Entrada"] = data_entrada
            if quantidade:
                produto["Quantidade"] = int(quantidade)
            if valor_entrada:
                produto["Valor de Entrada"] = float(valor_entrada)
                produto["Valor de Venda Sugerido"] = float(valor_entrada) * 1.35
            print(f"Produto {codigo} atualizado com sucesso.")
            return
    print(f"Produto com código {codigo} não encontrado.")

# Venda/Retirada
def efetuar_venda(codigo, quantidade):
    for produto in produtos:
        if produto["Codigo"] == codigo:
            if produto["Quantidade"] >= quantidade:
                produto["Quantidade"] -= quantidade
                print(f"Venda realizada: {quantidade} unidades de {produto['Nome']}.")
                return
            else:
                print("Quantidade solicitada maior que a disponível.")
                return
    print(f"Produto com código {codigo} não encontrado.")

# Salvar em JSON
def salvar_em_json(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)
    print(f"Dados salvos em {nome_arquivo} com sucesso.")

# Recuperar os produtos do JSON
def recuperar_de_json(nome_arquivo):
    global produtos
    try:
        with open(nome_arquivo, 'r') as arquivo:
            produtos = json.load(arquivo)
        print(f"Dados recuperados de {nome_arquivo} com sucesso.")
        for produto in produtos:
            print("\nProduto:")
            for chave, valor in produto.items():
                print(f"{chave}: {valor}")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Inicializando lista de produtos vazia.")
        produtos = []

# Menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Incluir Produto")
        print("2. Atualizar Produto")
        print("3. Efetuar Venda")
        print("4. Salvar Produtos")
        print("5. Recuperar Produtos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            tipo = input("Tipo do produto: ")
            data_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            quantidade = int(input("Quantidade: "))
            valor_entrada = float(input("Valor de entrada: "))
            incluir_produto(codigo, nome, tipo, data_entrada, quantidade, valor_entrada)

        elif opcao == '2':
            codigo = input("Código do produto a atualizar: ")
            nome = input("Novo nome (deixe vazio para não alterar): ")
            tipo = input("Novo tipo (deixe vazio para não alterar): ")
            data_entrada = input("Nova data de entrada (deixe vazio para não alterar): ")
            quantidade = input("Nova quantidade (deixe vazio para não alterar): ")
            valor_entrada = input("Novo valor de entrada (deixe vazio para não alterar): ")
            atualizar_produto(
                codigo,
                nome,
                tipo,
                data_entrada,
                quantidade,
                valor_entrada
            )

        elif opcao == '3':
            codigo = input("Código do produto a vender: ")
            quantidade = int(input("Quantidade a vender: "))
            efetuar_venda(codigo, quantidade)

        elif opcao == '4':
            salvar_em_json("produtos.json")

        elif opcao == '5':
            recuperar_de_json("produtos.json")

        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
