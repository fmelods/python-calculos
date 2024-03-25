# 1. Faça um Programa que peça dois números e imprima a soma.
num1 = (int(input("Digite o primeiro número: ")))
num2 = (int(input("Digite o segundo número: ")))
soma = num1 + num2
print("A soma dos números é: ", soma)

print()

# 2. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
fahrenheit = (float(input("Digite a temperatura em Fahrenheit: ")))
celsius = (fahrenheit - 32) * 5/9
print("A temperatura em Celsius é: ", celsius)

print()

# 3. Faça um programa que solicite o salário do usuário e calcule o novo salário com o aumento de 18%. O programa deverá exibir o valor do aumento e o novo salário.
salario = (float(input("Digite o salário: ")))
aumento = salario * 0.18
novo_salario = salario + aumento
print("O aumento foi de: ", aumento)
print("O novo salário é: ", novo_salario)

print()

# 4. Escrever um algoritmo que lê as 4 notas obtidas por um aluno. Calcular a média ponderada de acordo com a seguinte fórmula: (Nota1 + Nota2 x 2 + Nota3 x 3 + Nota4 x 4) / 10.
nota1 = (float(input("Digite a primeira nota: ")))
nota2 = (float(input("Digite a segunda nota: ")))
nota3 = (float(input("Digite a terceira nota: ")))
Nota4 = (float(input("Digite a quarta nota: ")))
media_ponderada = (nota1 + nota2 * 2 + nota3 * 3 + Nota4 * 4) / 10
print("A média ponderada é: ", media_ponderada)

print()

# 5. Faça um programa que solicite dois números para o usuário, sendo o primeiro a base e segundo o expoente. Calcule o primeiro número elevado ao segundo número e exiba o valor na tela.
base = (int(input("Digite a base: ")))
expoente = (int(input("Digite o expoente: ")))
resultado = base ** expoente
print("O resultado é: ", resultado)

print()

# 6. Faça um programa que solicite a idade do usuário e exiba a quantidade de dias que o usuário já viveu
idade = (int(input("Digite a sua idade: ")))
dias_vividos = idade * 365
print("Você já viveu: ", dias_vividos, "dias")

print()

# 7. Faça um programa que solicite a distância percorrida em uma determinada viagem e a quantidade de combustível gasto neste percurso. Calcule o consume do veículo em km/l.
distancia = (float(input("Digite a distância percorrida: ")))
combustivel = (float(input("Digite a quantidade de combustível gasto: ")))
consumo = distancia / combustivel
print("O consumo do veículo é: ", consumo, "km/l")

print()

# 8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor de desconto e o preço a pagar.
preco = (float(input("Digite o preço da mercadoria: ")))
desconto = (float(input("Digite o percentual de desconto: ")))
valor_desconto = preco * (desconto / 100)
preco_pagar = preco - valor_desconto
print("O valor do desconto é: ", valor_desconto)

print()