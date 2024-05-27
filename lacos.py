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
while num != 0:
    if num % 2 != 0:
        print(f"Número: {num}")
    num = num - 1

print()

