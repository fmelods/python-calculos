# 1 exercícios a-m (cálculo)
a = 11
b = 3
print(a+b*a)
print(b * a+b)
print(a // b)
print(b % a)
print(a % b)
print(b//a)
print(b-a/b)
print(a/b-a*b)
print(10+a % b)
print(10-b//a)
print(b//a-50)
print(a+b % a-a//b*2)
print(a*(b+a)-(a-b)/2)

print()

# 2 exercícios a-m (true and false)
x = True
y = False
print(x and y)
print(x or y)
print(x and y or x)
print(x or y or x)
print(not (x or not y))
print(not (not x and not y))
print(not (not x and not y))
print(not x and y)
print(not (x and y))
print(not x and y or x)
print(not (x and y) and y)
print(x and y or y and not x)
print(not (x or y and y or y))

print()

# 3 exercícios a-7 (cálculo + true and false)
a = 5
b = 9
x = not True
y = False and True
m = "casa"
n = "mesa"
print(x and y == x or y)
print(a*b <= b - a)
print(not (a == b or not b != a))
print(not (m != n and b > a))
print(b+a <= a*b and y)
print(x and not y or a//b != a % b)

print()

# 1 - Lista 1 (alô mundo)
print(f"alô mundo")

print()

# 2 - Lista 1 (número informado)
num1 = float(input("digite um número: "))
print(f"o número informado foi:", num1)

print()

# 3 - Lista 1 (soma)
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
print(f"a soma dos dois números é:", num1+num2)

print()

# 4 - Lista 1 (média global)
nota1 = float(input("digite a nota do primeiro bimestre: "))
nota2 = float(input("digite a nota do segundo bimestre: "))
nota3 = float(input("digite a nota do terceiro bimestre: "))
nota4 = float(input("digite a nota do quarto bimestre: "))
media = (nota1+nota2+nota3+nota4) / 4
print(f"a sua média global é:", media)

print()

# 5 - Lista 1 (conversão para cm)
metro = float(input("digite uma metragem para ser convertida em cm: "))
conversao = (metro*100)
print(conversao, "cm")

print()

# 6 - Lista 1 (área de um círculo)
raio = float(input("digite o raio de um círculo: "))
calculo = (2*3.14*raio)
print(f"a área do círculo é", calculo)

print()

# 7 - Lista 1 (área de um quadrado e o dobro)
lado = float(input("digite o comprimento do lado do quadrado: "))
area = (lado**2)
dobro_area = (2*area)
print(f"a área do quadrado é", area)
print(f"o dobro da área do quadrado é:", dobro_area)

print()

# 8 - Lista 1 (salário mensal por horas trabalhadas)
ganho_hora = float(input("digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("digite a sua quantidade de horas trabalhadas no mês: "))
calculo_horas = (ganho_hora / 30 * horas_trabalhadas) * 30
print(f"o seu salário total é:", "R$", calculo_horas, "ao mês")

print()

# 9 - Lista 1 (fahreinheit para celsius)
temperatura_fahreinheit = float(input("digite uma temperatura em graus fahrenheint: "))
calculo_celsius = (5*(temperatura_fahreinheit - 32) / 9)
print(f"a temperatura em celsius é:", calculo_celsius)

print()

# 10 - Lista 1 (celsius para fahreinheit)
temperatura_celsius = float(input("digite uma temperatura em graus celsius: "))
calculo_fahreinheit = (temperatura_celsius*9) / 5 + 32
print(f"a temperatura em fahreinheit é:", calculo_fahreinheit)

print()

# 11 - Lista 1 (cálculo de número inteiro e real)
num1 = int(input("digite um número inteiro: "))
num2 = int(input("digite outro número inteiro: "))
num3 = float(input("digite um número real: "))
print(float(num1*2)*(num2/2))
print(float(num1*3+num3))
print(float(num3**3))

print()

# 12 - Lista 1 (peso ideal por altura)
altura = float(input("digite sua altura (em metros): "))
peso_ideal = ((72.7*altura) - 58)
print(f"seu peso ideal é:", peso_ideal)

print()

# 13 - Lista 1 (peso ideal por altura e gênero)
altura = float(input("digite sua altura (em metros): "))
genero = input("digite seu gênero (m para masculino, f para feminino): ")
if genero == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"o peso ideal para um homem com altura {altura}m é: {peso_ideal}kg")
elif genero == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"o peso ideal para uma mulher com altura {altura}m é: {peso_ideal}kg")
else:
    print("gênero não reconhecido. por favor, insira m para masculino ou f para feminino.")

print()

# 14 - Lista 1 (limite regular de peso de peixes)
peso = float(input("Digite o peso de peixes (em quilos): "))
limite_regulamentar = 50.0
if peso > limite_regulamentar:
    excesso = peso - limite_regulamentar
    multa = excesso * 4.00
    print(f"Peso de peixes: {peso}kg")
    print(f"Limite regulamentar: {limite_regulamentar}kg")
    print(f"Excesso: {excesso}kg")
    print(f"Multa a ser paga: R${multa:.2f}")
else:
    print("Peso dentro do limite regulamentar. Nenhuma multa será aplicada.")

print()

# 15 - Lista 1 (salário líquido com descontos de impostos)
valor_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = valor_por_hora * horas_trabalhadas
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"- IR (11%): R${imposto_renda:.2f}")
print(f"- INSS (8%): R${inss:.2f}")
print(f"- Sindicato (5%): R${sindicato:.2f}")
print(f"= Salário Líquido: R${salario_liquido:.2f}")

print()

# 16 - Lista 1 (preço total para pintura)
import math
area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_tinta = area_pintada / 3
latas_necessarias = math.ceil(litros_tinta / 18)
preco_total = latas_necessarias * 80.00
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R${preco_total:.2f}")

print()

# 17 - Lista 1 (melhor custo benefício para pintura)
import math
area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 1 / 6
litros_por_lata = 18
preco_lata = 80.00
litros_por_galao = 3.6
preco_galao = 25.00
litros_necessarios = area_pintada * cobertura_por_litro * 1.1
latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
preco_total_latas = latas_necessarias * preco_lata
galoes_necessarios = math.ceil(litros_necessarios / litros_por_galao)
preco_total_galoes = galoes_necessarios * preco_galao
latas_combinacao = math.floor(litros_necessarios / litros_por_lata)
galoes_combinacao = math.ceil((litros_necessarios % litros_por_lata) / litros_por_galao)
preco_total_combinacao = (latas_combinacao * preco_lata) + (galoes_combinacao * preco_galao)
print(f"Quantidade de tinta necessária: {litros_necessarios:.2f} litros")
print("\nOpção 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R${preco_total_latas:.2f}")
print("\nOpção 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {galoes_necessarios}")
print(f"Preço total: R${preco_total_galoes:.2f}")
print("\nOpção 3: Misturar latas e galões")
print(f"Quantidade de latas: {latas_combinacao}")
print(f"Quantidade de galões: {galoes_combinacao}")
print(f"Preço total: R${preco_total_combinacao:.2f}")

print()

# 18 - Lista 1 (tempo de download)
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade da Internet (em Mbps): "))
tempo_download_minutos = (tamanho_arquivo_mb / (velocidade_internet_mbps / 8)) / 60
print(f"O tempo aproximado de download será de {tempo_download_minutos:.2f} minutos.")

print()

# 1 - Lista 2 (aluguel de carro)
valor_diario = 60
valor_km = 0.15
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de km rodados: "))
valor_total = (dias*valor_diario) + (km*valor_km)
print(f"O valor total do aluguel é de R${valor_total:.2f}")

print()

# 2 - Lista 2 (tempo perdido de um fumante)
minutos_perdidos_por_cigarro = 10
cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos que você fuma: "))
cigarros_total = (cigarros_dia*anos_fumando*365)
perda_minutos_total = (cigarros_total*minutos_perdidos_por_cigarro)
perda_dias_total = perda_minutos_total / (60*24)
print(f"Você perdeu {perda_dias_total:.2f} dias de vida.")

print()

# 3 - Lista 2 (Cadastro do usuário)
nome_completo = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (M/F): ").upper()
estado_civil = input("Digite seu estado civil: ")
salario = float(input("Digite seu salário: "))
anos_trabalhados = float(input("Digite quantos anos você já trabalhou: "))
def dias_uteis():
  dias_ano = 365
  sabados_domingos = 52 * 2
  feriados = 10
  return dias_ano - sabados_domingos - feriados
dias_trabalhados = anos_trabalhados * dias_uteis()
horas_trabalhadas = dias_trabalhados * 8
anos_aposentadoria = 90 - (idade + anos_trabalhados)
print(f"Nome completo:", nome_completo.upper())
print(f"Nome completo:", nome_completo.lower())
print(f"Nome completo:", nome_completo.title())
print(f"Idade:", idade)
print(f"Gênero:", genero)
print(f"Estado civil:", estado_civil)
print(f"Salário:", salario)
print(f"Anos trabalhados:", anos_trabalhados)
print(f"Dias trabalhados:", dias_trabalhados)
print(f"Horas trabalhadas:", horas_trabalhadas)
print(f"Anos para se aposentar:", anos_aposentadoria)

print()

# 1 - Lista 3 (viagem de carro)
distancia_a_percorrer = float(input("Digite a distância a ser percorrida com o carro: "))
velocidade_media_esperada = float(input("Digite a velocidade média esperada para a viagem: "))
tempo_de_viagem = (distancia_a_percorrer / velocidade_media_esperada)
print(f"O tempo até você completar sua viagem é: {tempo_de_viagem:.2f} hora.")

print()

# 2 - Lista 3 (cédulas do caixa eletrônico que dispensa 50, 20 e 10)
def caixa_eletronico():
  notas = [50, 20, 10]
  qtd_notas = {nota: 0 for nota in notas}
  valor = int(input("Digite o valor a ser sacado (múltiplo de 10): "))
  if valor % 10 != 0:
    print("Valor inválido! Digite um valor múltiplo de 10.")
    return
  for nota in notas:
    qtd_notas[nota] = valor // nota
    valor %= nota
  print("Relatório de notas:")
  for nota, qtd in qtd_notas.items():
    print(f"- {nota} reais: {qtd}")
caixa_eletronico()
print()

# 3 - Lista 3 (empréstimo bancário)
def aprovar_emprestimo():
    valor_casa = float(input("Digite o valor do imóvel: R$ "))
    salario = float(input("Digite o seu salário: R$ "))
    anos_pagar = int(input("Digite a quantidade de anos para pagar: "))
    prestacao_mensal = valor_casa / (anos_pagar * 12)
    porcentagem_salario = prestacao_mensal / salario * 100
    if porcentagem_salario <= 30:
        print("Empréstimo aprovado!")
        print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
        print(f"Porcentagem do salário comprometida: {porcentagem_salario:.2f}%")
    else:
        print("Empréstimo negado.")
        print(f"Valor da prestação mensal excede 30% do seu salário.")
        print(f"Porcentagem do salário comprometida: {porcentagem_salario:.2f}%")      
aprovar_emprestimo()

print()

# 4 - List 3 (quantidade de horas e minutos)
def converter_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    saída = f"{horas}h{minutos_restantes}m"
    return saída
tempo_minutos = int(input("Digite a quantidade de minutos: "))
tempo_convertido = converter_minutos(tempo_minutos)
print(f"Tempo convertido: {tempo_convertido}")
print()

# 5 - Lista 3 (quantidade horas, minutos e segundos)
def converter_segundos(segundos):
    horas = segundos // 3600
    minutos_restantes = (segundos % 3600) // 60
    segundos_restantes = (segundos % 3600) % 60
    saida = f"{horas}h{minutos_restantes}m{segundos_restantes}s"
    return saida
tempo_segundos = int(input("Digite a quantidade de segundos: "))
tempo_convertido = converter_segundos(tempo_segundos)
print(f"Tempo convertido: {tempo_convertido}")

print()
