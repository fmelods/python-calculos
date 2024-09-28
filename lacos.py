# 1 - 1 a 100
num = 0
while num != 100:
    num = num + 1
    print(f"Número: {num}")

print()

# 2 - 50 a 100
num = 49
while num != 100:
    num = num + 1
    print(f"Número: {num}")

print()

# 3 - Contagem regressiva
num = 11
while num != 0:
    num = num - 1
    print(f"Número: {num}")

print()

# 4 - Imprimir de 1 até o numéro digitado, com apenas números ímpares
num = 0
num = int(input("Digite um número: "))
count = 1
while count <= num:
    if count % 2 != 0:
        print(f"Número: {count}")
    count += 1

# 5 - Multiplicação sucessiva
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

result = 0
count = 0

while count < num2:
    result += num1
    count += 1

print(f"O resultado da multiplicação é: {result}")

# 6 - quantidade de números inteiros
def main():
    numeros = []

    while True:
        numero = int(input("Digite um número inteiro ou 0 para finalizar a execução: "))
        if numero == 0:
            break
        numeros.append(numero)

    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade if quantidade > 0 else 0

    print(f"\nQuantidade de números: {quantidade}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")

    if __name__ == "__main__":
        main()

# 7 - juros na poupança
def calcular_poupanca():
    deposito_inicial = float(input("Digite o valor do depósito inicial: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100

    saldo = deposito_inicial
    total_juros = 0

    print("\nMês | Saldo")
    print("-" * 20)

    for mes in range(1, 25):
        juros = saldo * taxa_juros
        saldo += juros
        total_juros += juros
        print(f"{mes:2d}")

    print("\nTotal ganho com juros no período: R${total_juros:,.2f}")

if __name__ == "__main__":
    calcular_poupanca()

# 8 - depósito mensal (aporte)
def calcular_poupanca():
    deposito_inicial = float(input("Digite o valor do depósito inicial: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
    aporte = float(input("Digite o valor do depósito mensal: "))

    saldo = deposito_inicial
    total_juros = 0

    print("\nMês | Saldo")
    print("-" * 20)

    for mes in range(1, 25):
        if mes > 1:
            saldo += aporte
        juros = saldo * taxa_juros
        saldo += juros
        total_juros += juros
        print(f"{mes:2d}   |  R${saldo:,.2f}")

    print(f"\nTotal de juros ganhos: R${total_juros:,.2f}")

if __name__ == "__main__":
    calcular_poupanca()

# 9 - meses, total pago e total de juros pago
divida = float(input("Informe o valor inicial da dívida: "))
juros_mensal = float(input("Informe o valor dos juros mensais (%): "))
pagamento_mensal = float(input("Informe o valor que será pago mensalmente: "))

meses = 0
total_pago = 0
total_juros = 0

while divida > 0:
    juros = divida * juros_mensal
    total_juros += juros
    divida += juros
    divida -= pagamento_mensal
    total_pago += pagamento_mensal
    meses += 1

print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R${total_pago:2f}")
print(f"Total de juros pagos: R${total_juros:2.f}")

# 10 - máquina registradora
precos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00
}

total_compra = 0

while True:
    codigo = int(input("Digite o código do produto (0 para sair): "))

    if codigo == 0:
        break
    elif codigo in precos:
        quantidade = int(input("Digite a quantidade comprada: "))
        total_compra += precos[codigo] * quantidade
    else:
        print("Código inválido.")

print(f"Total das compras: R$ {total_compra:.2f}")

# 11 - verificar se um número é primo
numero = int(input("Digite um número: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
        if primo:
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")

# 12 - n números primos
# Imprimir os n primeiros números primos
n = int(input("Digite a quantidade de números primos a exibir: "))

contagem = 0
numero = 2

while contagem < n:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero, end=" ")
        contagem += 1
    numero += 1

# 13 - mínimo, máximo e médio
quantidade = int(input("Quantos números deseja inserir? "))
numeros = []

for _ in range(quantidade):
    num = int(input("Digite um número: "))
    numeros.append(num)

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / quantidade

print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")
print(f"Valor médio: {media:.2f}")

# 14 - sequência de fibonacci
n = int(input("Digite o valor de N para a sequência de Fibonacci: "))
fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print(", ".join(map(str, fibonacci[:n])))

# 15 - fatorial
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(2, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")

# 16 - equação com valor de n
import math

def calcular_soma(n):
    soma = 0
    for i in range(1, n+1):
        soma += i / math.factorial(2*i - 1)
    return soma

n = int(input("Digite o valor de n: "))
resultado = calcular_soma(n)
print(f"O resultado da soma para n={n} é: {resultado}")


# 17 - valores de n e k
import math

def calcular_soma_n_k(n, k):
    soma = 0
    for i in range(k, n+1):
        soma += i / math.factorial(2*i)
    return soma

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

if n >= k >= 0:
    resultado = calcular_soma_n_k(n, k)
    print(f"O resultado da soma para n={n} e k={k} é: {resultado}")
else:
    print("Os valores de n e k devem satisfazer n >= k >= 0")

# 18 - equação
import math
n = int(input("Digite o valor de n: "))
soma = 0
for i in range(1, n + 1):
    termo = i / math.factorial(2 * i - 1)
    soma += termo
print(f"O resultado da soma é: {soma:.6f}")
