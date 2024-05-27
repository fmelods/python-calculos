# 1 - Exercício de enfileiramento de pacientes de um hospital
fila = []

def enfileirar_paciente():
    paciente = input("Digite a área de atendimento do paciente (G para Clínico Geral, O para Ortopedia, C para Cardiologia, P para Pediatra, F para Oftalmologia): ")
    fila.append(paciente)

def cadastrar_paciente():
    if len(fila) == 0:
        print("Não há pacientes na fila.")
        return
    
    paciente = fila.pop(0)
    nome = input("Digite o nome do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    carteirinha = input("Digite o número da carteirinha do paciente: ")
    data_hora_atendimento = input("Digite a data e hora de atendimento do paciente: ")
    sintomas = input("Digite uma breve descrição dos sintomas do paciente: ")
    
    # Armazenar as informações em listas em memória
    # Exemplo:
    # pacientes.append({
    #     "nome": nome,
    #     "endereco": endereco,
    #     "carteirinha": carteirinha,
    #     "area_atendimento": paciente,
    #     "data_hora_atendimento": data_hora_atendimento,
    #     "sintomas": sintomas
    # })
    
    print("Paciente cadastrado com sucesso.")

def exibir_relatorio():
    if len(pacientes) == 0:
        print("Não há pacientes cadastrados.")
        return
    
    for paciente in pacientes:
        print("Nome:", paciente["nome"])
        print("Endereço:", paciente["endereco"])
        print("Carteirinha:", paciente["carteirinha"])
        print("Área de Atendimento:", paciente["area_atendimento"])
        print("Data e Hora de Atendimento:", paciente["data_hora_atendimento"])
        print("Sintomas:", paciente["sintomas"])
        print("--------------------")

while True:
    print("1 - Enfileirar Paciente")
    print("2 - Cadastrar Paciente")
    print("3 - Exibir Relatório")
    print("4 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        enfileirar_paciente()
    elif opcao == "2":
        cadastrar_paciente()
    elif opcao == "3":
        exibir_relatorio()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Digite novamente.")

# 2 - # Plano passo a passo:
# 1. Criar listas vazias para produtos, clientes e vendas
# 2. Criar um loop while para o menu
# 3. Dentro do loop, usar declarações if-elif-else para lidar com a escolha do usuário
# 4. Para cada opção, criar uma função que realiza a tarefa necessária

produtos = []
clientes = []
vendas = []

def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    data_cadastro = input("Digite a data de cadastro: ")
    valor_compra = float(input("Digite o valor de compra: "))
    valor_venda = float(input("Digite o valor de venda: "))
    quantidade_estoque = int(input("Digite a quantidade em estoque: "))
    produtos.append([codigo, nome, data_cadastro, valor_compra, valor_venda, quantidade_estoque])

def cadastrar_cliente():
    codigo = input("Digite o código do cliente: ")
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")
    clientes.append([codigo, nome, endereco, email])

def realizar_venda():
    codigo_cliente = input("Digite o código do cliente: ")
    codigo_produto = input("Digite o código do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    for produto in produtos:
        if produto[0] == codigo_produto:
            if produto[5] >= quantidade:
                produto[5] -= quantidade
                vendas.append([codigo_cliente, codigo_produto, quantidade, produto[4]*quantidade])
                print("Venda realizada!")
                return
            else:
                print("Estoque insuficiente!")
                return
    print("Produto não encontrado!")

def relatorio_estoque():
    for produto in produtos:
        print(f"Código: {produto[0]}, Nome: {produto[1]}, Estoque: {produto[5]}")

def relatorio_vendas():
    vendas_totais = 0
    lucro_total = 0
    for venda in vendas:
        vendas_totais += venda[3]
        for produto in produtos:
            if produto[0] == venda[1]:
                lucro_total += (produto[4] - produto[3]) * venda[2]
    print(f"Vendas totais: {vendas_totais}, Lucro total: {lucro_total}")

while True:
    print("1 - Cadastrar Produto")
    print("2 - Cadastrar Cliente")
    print("3 - Realizar Venda")
    print("4 - Relatório de Estoque")
    print("5 - Relatório de Vendas")
    print("6 - Sair")
    opcao = input("Digite sua opção: ")
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        cadastrar_cliente()
    elif opcao == "3":
        realizar_venda()
    elif opcao == "4":
        relatorio_estoque()
    elif opcao == "5":
        relatorio_vendas()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")