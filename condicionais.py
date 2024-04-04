from datetime import datetime

# Lista da Aula 8 - Exercícios de IF e ELSE
# 1 - Positivo ou não
numero = float(input("Digite um número: "))
if numero > 0:
    print(f"O número é positivo")
else:
    print(f"O número não é positivo")

print()

# 2 - Menor ou maior de idade
idade = int(input("Digite sua idade: "))
if idade < 18:
    print(f"Você é menor de idade")
else:
    print(f"Você é maior de idade")

print()

# 3 - Par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O Número é par")
else:
    print(f"O Número é ímpar")

print()

# 4 - Maior número
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num1 < num2:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print(f"Os números são iguais")

print()

# 5 - Média e aprovação/reprovação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = nota1 + nota2 / 2
if media < 5:
    print(f"Você está reprovado")
else:
    print(f"Você está aprovado")

print()

# 6 - Nota válida ou inválida
nota = float(input("Digite uma nota: "))
if nota >= 0 and nota <= 10:
    print(f"Nota válida")
else:
    print(f"Nota inválida")

print()

# 7 - Nota válida ou inválida e média de aprovação/reprovação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    if media < 5:
        print(f"Você está reprovado")
    else:
        print(f"Você está aprovado")
else:
    print(f"Nota inválida")

print()

# 8 - Positivo, negativo ou nulo
numero = float(input("Digite um número: "))
if numero > 0
    print(f"O número é positivo")
if numero < 0
    print(f"o número é negativo")
else:
    print(f"O número é nulo")

# 9 - média de 3 notas e aprovação/reprovação (menor nota descartada)
av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))
av3 = float(input("Digite a nota da AV3: "))
if av1 < av2 and av1 < av3:
    media = (av2 + av3) / 2
    elif av2 < av1 and av2 < av3
    media = (av1 + av3) / 2
else:
    media = (av1 + av2) / 2
    if media < 6:
        print(f"Reprovado")
    else:
        print(f"Aprovado")

print()

# 10 - Maior valor entre 3 números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior")
else:
    print(f"O número {num3} é o maior")

print()

# 11 - Cálculo de INSS por salário
salario = float(input("Digite o salário: "))
if salario <= 1247.70:
    inss = salario * 0.08
elif salario > 1247.70 and salario <= 2079.50:
    inss = salario * 0.09
elif salario > 2079.50 and salario <= 4159.00: 
    inss = salario * 0.11
else: 
    inss = 468.00
    print(f"O valor do INSS é de R${inss:.2f}")

print()

# 12 - Cálculo de IR por salário
salario = float(input("Digite o salário: "))
if salario <= 1710.78:
    ir = 0
elif salario > 1710.78 and salario <= 2563.91:
    ir = salario * 0.075 - 128.31
elif salario > 2563.91 and salario <= 3418.59:
    ir = salario * 0.15 - 320.60
elif salario > 3418.59 and salario <= 4271.59:
    ir = salario * 0.225 - 577.00
else:
    ir = salario * 0.275 - 790.58
    print(f"O valor do IR é de R${ir:.2f}")

print()

# 13 - Cálculo de INSS e de IR por salário - exibição de salário líquido
salario_bruto = float(input("Digite o salário bruto: "))

# Cálculo do INSS
if salario_bruto <= 1247.70:
    inss = salario_bruto * 0.08
elif salario_bruto <= 2079.50:
    inss = salario_bruto * 0.09
elif salario_bruto <= 4159.00: 
    inss = salario_bruto * 0.11
else: 
    inss = 468.00

# Cálculo do IR
if salario_bruto <= 1710.78:
    ir = 0
elif salario_bruto <= 2563.91:
    ir = salario_bruto * 0.075 - 128.31
elif salario_bruto <= 3418.59:
    ir = salario_bruto * 0.15 - 320.60
elif salario_bruto <= 4271.59:
    ir = salario_bruto * 0.225 - 577.00
else:
    ir = salario_bruto * 0.275 - 790.58

# Cálculo do Salário Líquido
salario_liquido = salario_bruto - inss - ir

# Exibição dos resultados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"IR: R${ir:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")

print()

# 14 - Três números em ordem crescente
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(f"{num1}, {num2}, {num3}")
    else:
        print(f"{num1}, {num3}, {num2}")
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num2}, {num3}, {num1}")
else:
    if num1 < num2:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num3}, {num2}, {num1}")

print()

# 15 - Dados três números pelo usuário, analisá-los e exibir a mensagem “3 números diferentes”, “2 dos 3 são iguais” ou “3 números iguais”.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 == num2 and num1 == num3:
    print("3 números iguais")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("2 dos 3 números são iguais")
else:
    print("3 números diferentes")

print()

# 16 - Porcentagem de convênio médico por idade e sexo
salario = float(input("Digite o salário: "))
sexo = int(input("Digite o sexo (1 para Masculino e 2 para Feminino): "))
idade = int(input("Digite a idade: "))
if idade <= 20:
    if sexo == 1:
        convenio = salario * 0.0534
    else:
        convenio = salario * 0.0356
elif idade <= 40:
    if sexo == 1:
        convenio = salario * 0.0844
    else:
        convenio = salario * 0.0643
else:
    if sexo == 1:
        convenio = salario * 0.1012
    else:
        convenio = salario * 0.0802
    print(f"O valor do convênio médico é de R${convenio:.2f}")

print()

# 17 - Média provas
prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
atividade1 = float(input("Digite a nota da primeira atividade: "))
atividade2 = float(input("Digite a nota da segunda atividade: "))
atividade3 = float(input("Digite a nota da terceira atividade: "))
atividade4 = float(input("Digite a nota da quarta atividade: "))
media_provas = (prova1 + prova2) / 2
media_atividades = (atividade1 + atividade2 + atividade3 + atividade4) / 4
av1 = media_provas * 0.6 + media_atividades * 0.4
if av1 > 6:
    print(f"AV1 = {av1:.1f}, você está acima da média")
elif av1 == 6:
    print(f"AV1 = 6.0, você está na média")
else:
    print(f"AV1 = {av1:.1f}, você está abaixo da média")

print()

# 18 - Nùmeros não diferentes
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 != num2 and num1 != num3:
    print(num1)
elif num2 != num1 and num2 != num3:
    print(num2)
elif num3 != num1 and num3 != num2:
    print(num3)
else:
    print("Os números não são diferentes")

print()

# 19 - Lados do triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")

print()

# 20 - Tipos de triângulos
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não forma um triângulo")

print()

# 21 - Dado o ano pelo usuário, verificar se o ano é bissexto exibindo a mensagem “Ano bissexto” ou “Não é ano bissexto”. Sabe-se que o ano bissexto é aquele que é múltiplo de 4, exceto os múltiplos de 100 que não sejam múltiplos de 400. Por exemplo: 1996, 2004, 2008, 2012, 1600, 2000 e 2400 (são bissextos); 1700, 1800, 1900 e 2100 (não são bissextos).
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Não é ano bissexto")

print()

# List da Aula 9 - Exercícios de Laços
# 1 - Exibir os 10 primeiros múltiplos de um número
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(numero * i)

print()

# 2 - Exibir em formato de tabuada
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print()

# 3 - Pedir o multiplicando e exibir no formato de tabuada
multiplicando = int(input("Digite o multiplicando: "))
for i in range(1, 11):
    print(f"{multiplicando} x {i} = {multiplicando * i}")

print()

# 4 - Somar números até que seja digitado zero
soma = 0
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    soma += numero
print(f"A soma dos números é {soma}")

print()

# 5 - Em uma votação, existem 3 candidatos: 1 – Huguinho, 2 – Zezinho e 3 – Luizinho. Pedir e acumular votos até que em votos seja digitado o numero 0 (zero). Ao final, exibir a quantidade de votos de cada usuário.
votos_huguinho = 0
votos_zezinho = 0
votos_luizinho = 0
voto = 1
while voto != 0:
    voto = int(input("Digite o número do candidato (1 - Huguinho, 2 - Zezinho, 3 - Luizinho): "))
    if voto == 1:
        votos_huguinho += 1
    elif voto == 2:
        votos_zezinho += 1
    elif voto == 3:
        votos_luizinho += 1
print(f"Votos Huguinho: {votos_huguinho}")
print(f"Votos Zezinho: {votos_zezinho}")
print(f"Votos Luizinho: {votos_luizinho}")

print()

# Lista da Aula 10 - Exercícios de Condicionais
# 1 - Verificar se o usuário tem idade para votar.
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 16:
    print("Você não pode votar.")
elif 16 <= idade < 18 or idade > 70:
    print("Seu voto é facultativo.")
else:
    print("Seu voto é obrigatório.")

print()

# 2 - Verificar senha de acesso.
password = input("Digite a senha: ")

if password == "123mudar":
    print("ACESSO PERMITIDO.")
else:
    print("ACESSO NEGADO.")

print()

# 3 - 