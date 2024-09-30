import json
from datetime import datetime

# Lista para armazenar os veículos no pátio
veiculos = []

# Função para adicionar um veículo
def adicionar_veiculo():
    nome_cliente = input("Nome do cliente: ")
    modelo = input("Modelo do veículo: ")
    ano = input("Ano do veículo: ")
    descricao_problema = input("Descrição do problema: ")
    categorias = ["motor", "câmbio", "pneus", "freios", "sistema de suspensão", 
                  "sistema de arrefecimento", "funilaria", "elétrico", "tapeçaria", "apenas revisão"]
    
    print("Categorias de problema:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    
    categoria_problema = categorias[int(input("Selecione a categoria do problema (número): ")) - 1]
    
    veiculo = {
        "data_hora_entrada": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome_cliente": nome_cliente,
        "modelo": modelo,
        "ano": ano,
        "descricao_problema": descricao_problema,
        "categoria_problema": categoria_problema
    }
    
    veiculos.append(veiculo)
    print("Veículo adicionado com sucesso!")

# Função para emitir relatório
def emitir_relatorio():
    categorias_contagem = {}
    
    for veiculo in veiculos:
        categoria = veiculo["categoria_problema"]
        if categoria in categorias_contagem:
            categorias_contagem[categoria] += 1
        else:
            categorias_contagem[categoria] = 1
    
    print("Relatório de veículos por categoria de problema:")
    for categoria, contagem in categorias_contagem.items():
        print(f"{categoria}: {contagem} veículo(s)")

# Função para registrar a saída do veículo
def registrar_saida():
    nome_cliente = input("Nome do cliente: ")
    modelo = input("Modelo do veículo: ")
    
    for veiculo in veiculos:
        if veiculo["nome_cliente"] == nome_cliente and veiculo["modelo"] == modelo:
            descricao_servicos = input("Descrição dos serviços realizados: ")
            pecas_trocadas = input("Peças trocadas: ")
            
            veiculo["data_hora_saida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            veiculo["descricao_servicos"] = descricao_servicos
            veiculo["pecas_trocadas"] = pecas_trocadas
            
            print("Saída do veículo registrada com sucesso!")
            return
    
    print("Veículo não encontrado.")

# Função para salvar os dados em um arquivo JSON
def salvar_dados():
    with open('veiculos.json', 'w') as f:
        json.dump(veiculos, f, indent=4)
    print("Dados salvos com sucesso!")

# Menu principal
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar veículo")
        print("2. Emitir relatório")
        print("3. Registrar saída de veículo")
        print("4. Salvar dados")
        print("5. Sair")
        
        opcao = input("Selecione uma opção: ")
        
        if opcao == '1':
            adicionar_veiculo()
        elif opcao == '2':
            emitir_relatorio()
        elif opcao == '3':
            registrar_saida()
        elif opcao == '4':
            salvar_dados()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()