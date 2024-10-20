# aumento de salário usando dicionários
def calcular_abonos():
    funcionarios = {}
    total_abonos = 0
    total_minimo = 0
    maior_abono = 0
    while True:
        id_funcionario = input("Digite o ID do funcionário (ou 0 para encerrar): ")
        if id_funcionario == '0':
            break
        salario = float(input(f"Digite o salário do funcionário {id_funcionario}: "))
        
        # Calcula o abono
        abono = max(salario * 0.2, 100)
        if abono == 100:
            total_minimo += 1
        
        novo_salario = salario + abono
        funcionarios[id_funcionario] = {
            'salario': salario,
            'abono': abono,
            'novo_salario': novo_salario
        }
        
        total_abonos += abono
        if abono > maior_abono:
            maior_abono = abono
    
    print("\nResumo:")
    print("ID\tSalário\tAbono\tNovo Salário")
    for id_func, dados in funcionarios.items():
        print(f"{id_func}\t{dados['salario']:.2f}\t{dados['abono']:.2f}\t{dados['novo_salario']:.2f}")
    
    print(f"\nTotal de funcionários processados: {len(funcionarios)}")
    print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
    print(f"Funcionários que receberam o abono mínimo de R$100: {total_minimo}")
    print(f"Maior valor pago como abono: R$ {maior_abono:.2f}")

calcular_abonos()
