import json

def calcular_abono(salario):
    abono = salario * 0.2
    return max(abono, 100)

def ler_funcionarios():
    try:
        with open('funcionarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_funcionarios(funcionarios):
    with open('funcionarios.json', 'w') as f:
        json.dump(funcionarios, f, indent=4)

def criar_funcionario(funcionarios):
    id_funcionario = input("Digite o ID do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    abono = calcular_abono(salario)
    novo_salario = salario + abono

    funcionarios.append({
        "ID": id_funcionario,
        "Salario": salario,
        "Novo Salario": novo_salario,
        "Abono": abono
    })

    salvar_funcionarios(funcionarios)
    print("Funcionário adicionado com sucesso!")

def ler_funcionarios_detalhes(funcionarios):
    print("\nResumo:")
    for func in funcionarios:
        print(f"ID: {func['ID']}, Salário: {func['Salario']:.2f}, Novo Salário: {func['Novo Salario']:.2f}, Abono: {func['Abono']:.2f}")
    print(f"Total de funcionários processados: {len(funcionarios)}")
    total_abono = sum(func['Abono'] for func in funcionarios)
    total_minimo = sum(1 for func in funcionarios if func['Abono'] == 100)
    maior_abono = max(func['Abono'] for func in funcionarios)
    print(f"Total gasto com abonos: {total_abono:.2f}")
    print(f"Número de funcionários que receberam o valor mínimo de 100 reais: {total_minimo}")
    print(f"Maior valor pago como abono: {maior_abono:.2f}")

def atualizar_funcionario(funcionarios):
    id_funcionario = input("Digite o ID do funcionário a ser atualizado: ")
    for func in funcionarios:
        if func['ID'] == id_funcionario:
            salario = float(input("Digite o novo salário do funcionário: "))
            abono = calcular_abono(salario)
            func['Salario'] = salario
            func['Novo Salario'] = salario + abono
            func['Abono'] = abono
            salvar_funcionarios(funcionarios)
            print("Funcionário atualizado com sucesso!")
            return
    print("Funcionário não encontrado.")

def deletar_funcionario(funcionarios):
    id_funcionario = input("Digite o ID do funcionário a ser deletado: ")
    for func in funcionarios:
        if func['ID'] == id_funcionario:
            funcionarios.remove(func)
            salvar_funcionarios(funcionarios)
            print("Funcionário deletado com sucesso!")
            return
    print("Funcionário não encontrado.")

def main():
    funcionarios = ler_funcionarios()

    while True:
        print("\nMenu:")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Atualizar funcionário")
        print("4. Deletar funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_funcionario(funcionarios)
        elif opcao == "2":
            ler_funcionarios_detalhes(funcionarios)
        elif opcao == "3":
            atualizar_funcionario(funcionarios)
        elif opcao == "4":
            deletar_funcionario(funcionarios)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()