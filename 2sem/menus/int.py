# leitura de números inteiros
def exibir_numeros(numeros):
    print("\nNúmeros digitados:")
    for num in numeros:
        print(num, end=" ")
    print()

numeros = []
while True:
    try:
        num = int(input("Digite um número inteiro (0 para sair): "))
        if num == 0:
            break
        numeros.append(num)
    except ValueError:
        print("Número inválido. Tente novamente.")

# Exibindo os resultados
if numeros:
    exibir_numeros(numeros)
    print(f"Quantidade de números: {len(numeros)}")
    print(f"Soma dos números: {sum(numeros)}")
    print(f"Média aritmética: {sum(numeros)/len(numeros):.2f}")
    print(f"Menor número: {min(numeros)}")
    print(f"Maior número: {max(numeros)}")
else:
    print("Nenhum número foi digitado.")
