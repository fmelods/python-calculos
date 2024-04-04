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
if numero > 0:
    print(f"O número é positivo")
if numero < 0:
    print(f"o número é negativo")
else:
    print(f"O número é nulo")

# 9 - média de 3 notas e aprovação/reprovação (menor nota descartada)
av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))
av3 = float(input("Digite a nota da AV3: "))
if av1 < av2 and av1 < av3:
    media = (av2 + av3) / 2
elif av2 < av1 and av2 < av3:
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

# 15 - Números diferentes ou iguais
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

# 21 - Verificar se um ano é bissexto.
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

# 5 - Votação de 3 candidatos
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
# 1 - Verificar se o usuário tem idade para votar
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

# 2 - Verificar senha de acesso
password = input("Digite a senha: ")

if password == "123mudar":
    print("ACESSO PERMITIDO.")
else:
    print("ACESSO NEGADO.")

print()

# 3 - Valor de compra
quantidade = int(input("Digite a quantidade de maçãs: "))
if quantidade < 12:
    valor = quantidade * 0.30
else:
    valor = quantidade * 0.25
print(f"O valor total da compra é R${valor:.2f}")

print()

# 4 - Área de um polígono
lados = int(input("Digite o número de lados do polígono: "))
medida = float(input("Digite a medida do lado (em cm): "))
if lados == 3:
    area = (medida ** 2) * 3 ** 0.5 / 4
    print(f"TRIÂNGULO - Área: {area:.2f} cm²")
elif lados == 4:
    area = medida ** 2
    print(f"QUADRADO - Área: {area:.2f} cm²")
elif lados == 5:

    print("PENTÁGONO")
else:
    print("Polígono não identificado")

print()

# 5 - Identificação de polígonos
lados = int(input("Digite o número de lados do polígono: "))
medida = float(input("Digite a medida do lado (em cm): "))
if lados == 3:
    area = (medida ** 2) * 3 ** 0.5 / 4
    print(f"TRIÂNGULO - Área: {area:.2f} cm²")
elif lados == 4:
    area = medida ** 2
    print(f"QUADRADO - Área: {area:.2f} cm²")
elif lados == 5:
    print("PENTÁGONO")
elif lados < 3:
    print("NÃO É UM POLÍGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")

print()

# 6 - Tipos de triângulos
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 == lado2 and lado1 == lado3:
    print("EQUILÁTERO")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("ISÓSCELES")
else:
    print("ESCALENO")

print()

# 7 - Ângulos de um triângulo
angulo1 = float(input("Digite o primeiro ângulo: "))
angulo2 = float(input("Digite o segundo ângulo: "))
angulo3 = float(input("Digite o terceiro ângulo: "))
if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("RETÂNGULO")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("OBTUSÂNGULO")
else:
    print("ACUTÂNGULO")

print()

# 8 - Placar de jogo de futebol
gols_time1 = int(input("Digite a quantidade de gols do primeiro time: "))
gols_time2 = int(input("Digite a quantidade de gols do segundo time: "))

if gols_time1 > gols_time2:
    print("Vitória do primeiro time.")
elif gols_time1 < gols_time2:
    print("Vitória do segundo time.")
else:
    print("Empate.")

print()

# 9 - Vogal ou consoante
letra = input("Digite uma letra: ")
if letra in "aeiou":
    print("Vogal.")
else:
    print("Consoante.")

print()

# 10 - Média Artimética e Média Ponderada
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
if i % 2 == 0:
    media = (a + b + c) / 3
    print(f"Média Aritmética: {media:.2f}")
elif i > 10:
    media = (a * 2 + b * 3 + c * 4) / 9
    print(f"Média Ponderada: {media:.2f}")

print()

# 11 - Valor máximo e mínimo de uma sequência de 10 números
maximo = float("-inf")
minimo = float("inf")
soma = 0
for i in range(10):
    numero = int(input("Digite um número: "))
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    soma += numero
media = soma / 10
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Média: {media}")

print()

# 12 - Operação matemática
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
print(f"Resultado: {resultado}")

print()

# 13 - Preço a pagar pela quantidade de kWh consumida
kwh = float(input("Digite a quantidade de kWh consumida: "))
instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias e C para comércios): ")
if instalacao == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
elif instalacao == "C":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
elif instalacao == "I":
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
print(f"Preço a pagar: R${preco:.2f}")

print()

# 14 - IMC e classificação
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
imc = peso / altura ** 2
if imc < 20:
    print("Abaixo do normal")
elif 20 <= imc <= 25:
    print("Normal")
elif 25 < imc <= 30:
    print("Sobrepeso")
elif 30 < imc <= 35:
    print("Obesidade leve")
elif 35 < imc <= 40:
    print("Obesidade moderada")
else:
    print("Obesidade mórbida")

print()

# 15 - Lucro de venda
valor_compra = float(input("Digite o valor da compra: "))
if valor_compra < 20:
    valor_venda = valor_compra * 1.45
else:
    valor_venda = valor_compra * 1.30
print(f"Valor da venda: R${valor_venda:.2f}")

print()

# 16 - Bom dia, boa tarde e boa noite
nome = input("Digite seu nome: ")
hora = int(input("Digite a hora atual: "))
if 0 <= hora < 12:
    print(f"Bom dia, {nome}!")
elif 12 <= hora < 18:
    print(f"Boa tarde, {nome}!")
else:
    print(f"Boa noite, {nome}!")

print()

# 17 - Data válida ou inválida
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split("/"))
if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        print("Data válida.")
    else:
        print("Data inválida.")
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        print("Data válida.")
    else:
        print("Data inválida.")
else:
    if 1 <= dia <= 28:
        print("Data válida.")
    elif dia == 29 and (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        print("Data válida.")
    else:
        print("Data inválida.")

print()

# 18 - Quantidade de centenas
numero = int(input("Digite um número inteiro menor que 1000: "))
centenas = numero // 100
dezenas = numero % 100 // 10
unidades = numero % 10
if centenas == 1:
    centenas_str = "centena"
else:
    centenas_str = "centenas"
if dezenas == 1:
    dezenas_str = "dezena"
else:
    dezenas_str = "dezenas"
if unidades == 1:
    unidades_str = "unidade"
else:
    unidades_str = "unidades"
if centenas > 0:

    if dezenas > 0 and unidades > 0:
        print(f"{centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}")
    elif dezenas > 0:
        print(f"{centenas} {centenas_str}, {dezenas} {dezenas_str}")
    elif unidades > 0:
        print(f"{centenas} {centenas_str} e {unidades} {unidades_str}")
    else:
        print(f"{centenas} {centenas_str}")
elif dezenas > 0:
    if unidades > 0:
        print(f"{dezenas} {dezenas_str} e {unidades} {unidades_str}")
    else:
        print(f"{dezenas} {dezenas_str}")
else:
    print(f"{unidades} {unidades_str}")

print()

# 19 - Coeficientes de uma equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"Raiz: {raiz}")
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print(f"Raízes: {raiz1} e {raiz2}")

print()

# 20 - Raízes reais
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"Raiz: {raiz}")
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print(f"Raízes: {raiz1} e {raiz2}")

print()

# 21 - Perguntas sobre um crime
respostas = 0
resposta = input("Telefonou para a vítima? (s/n): ")
if resposta == "s":
    respostas += 1
resposta = input("Esteve no local do crime? (s/n): ")
if resposta == "s":
    respostas += 1
resposta = input("Mora perto da vítima? (s/n): ")
if resposta == "s":
    respostas += 1
resposta = input("Devia para a vítima? (s/n): ")
if resposta == "s":
    respostas += 1
resposta = input("Já trabalhou com a vítima? (s/n): ")
if resposta == "s":
    respostas += 1
if respostas == 2:
    print("Suspeita")
elif 3 <= respostas <= 4:
    print("Cúmplice")
elif respost
as == 5:
    print("Assassino")
else:
    print("Inocente")

print()

# 22 - Promoção de Carnes
tipo = input("Digite o tipo de carne (F - Filé Duplo, A - Alcatra, P - Picanha): ")
quantidade = float(input("Digite a quantidade de carne (em kg): "))
if quantidade <= 5:
    if tipo == "F":
        preco = 4.90
    elif tipo == "A":
        preco = 5.90
    else:
        preco = 6.90
else:
    if tipo == "F":
        preco = 5.80
    elif tipo == "A":
        preco = 6.80
    else:
        preco = 7.80
total = quantidade * preco
pagamento = input("Digite o tipo de pagamento (C - Cartão Tabajara, D - Dinheiro): ")
if pagamento == "C":
    desconto = total * 0.05
else:
    desconto = 0
total_pagar = total - desconto
print(f"Tipo de carne: {tipo}")
print(f"Quantidade de carne: {quantidade} kg")
print(f"Preço total: R${total:.2f}")
print(f"Tipo de pagamento: {pagamento}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_pagar:.2f}")
