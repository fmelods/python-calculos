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

