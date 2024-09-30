# vetor: v1 = [45, 89, 32, 12, 33]

# 1 - primeiro elemento do vetor
def primeiro_elemento(vetor):
    return vetor[0]
v1 = [45, 89, 32, 12, 33]
print(primeiro_elemento(v1))

# 2 - números negativos do vetor
def exibir_numeros_negativos(vetor):
    for numero in vetor:
        if numero < 0:
            print(numero)

v1 = [45, 89, 32, 12, 33]
exibir_numeros_negativos(v1)

# 3 - soma dos elementos do vetor
def soma_elementos(vetor):
    return sum(vetor)

v1 = [45, 89, 32, 12, 33]
print(soma_elementos(v1))

# 4 - mediados elementos do vetor
def mediana(vetor):
    if len(vetor) % 2 == 0:
        return vetor[len(vetor) // 2 - 1], vetor[len(vetor) // 2]
    else:
        return vetor[len(vetor) // 2]
    
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mediana(vetor))

print()

# 5 - números ímpares no vetor
def impares(vetor):
    for i in vetor:
        if i % 2 != 0:
            print(i)

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares(vetor)

print()

# 6 - primeiro e último elemento do vetor
def primeiro_ultimo(vetor):
    print(f"Primeiro elemento: {vetor[0]}")
    print(f"Último elemento: {vetor[-1]}")

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_ultimo(vetor)

print()

# 7 - números pares no vetor
def indices_pares(vetor):
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(vetor[i])

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indices_pares(vetor)

print()

# 8 - retornar true ou false de acordo com os elementos existentes no vetor
def existe(vetor, valor):
    for i in vetor:
        if i == valor:
            return True
    return False

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(existe(vetor, 5))
print(existe(vetor, 10))

print()

# 9 - ordernar os elementos do vetor
def ordenar(vetor):
    vetor.sort()
    return vetor

v1 = [41, 72, 39, 4, 35]
print(ordenar(v1))

print()

# 10 - copiar os elemento do vetor v1 e v2
def copia_vetor(v1, v2):
    for i in v1:
        v2.append(i)
    return v2

v1 = [41, 72, 39, 4, 35]
v2 = []
print(copia_vetor(v1, v2))

print()

# 11 - inverter os elementos dos vetores
def inverte_vetor(v1, v2):
    for i in range(len(v1)):
        v2.append(v1[len(v1) - i - 1])
    return v2

v1 = [41, 72, 39, 4, 35]
v2 = []
print(inverte_vetor(v1, v2))

print()

# 12 - ordernar de forma crescente o vetor passado por parâmetro
def ordena_vetor_crescente(v):
    v.sort()
    return v

v = [41, 72, 39, 4, 35]
print(ordena_vetor_crescente(v))

print()

# 13 - ordernar de forma decrescente o vetor passado por parâmetro
def ordena_vetor_decrescente(v):
    v.sort(reverse=True)
    return v

v = [41, 72, 39, 4, 35]
print(ordena_vetor_decrescente(v))

print()

# 14 - Fazer um procedimento chamado 'ordena_vetor(v, forma)' que baseado na forma ('c' para crescente ou 'd' para decrescente) ordene na ordem solicitada
def ordena_vetor(v, forma):
    if forma == 'c':
        v.sort()
    elif forma == 'd':
        v.sort(reverse=True)
    return v

v = [41, 72, 39, 4, 35]
print(ordena_vetor(v, 'c'))
print(ordena_vetor(v, 'd'))

print()

# 15 - Fazer um procedimento chamado 'separa_pares_impares(v)' que coloque nas posições mais à esquerda os valores pares e mais a diretia os impares
def separa_pares_impares(v):
    pares = []
    impares = []
    for i in v:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares + impares

v = [41, 72, 39, 4, 35]
print(separa_pares_impares(v))

print()

# 16 - Fazer uma função chamada 'conta_acima_media(v) que retorne quantos elementos do vetor estão acima da média.
def conta_acima_media(v):
    media = sum(v) / len(v)
    acima_media = 0
    for i in v:
        if i > media:
            acima_media += 1
    return acima_media

v = [41, 72, 39, 4, 35]
print(conta_acima_media(v))

print()

# 17 - Fazer uma função chamada 'maior_elemento(v)' que retorne o elemento de maior valor do vetor
def maior_elemento(v):
    return max(v)

v = [41, 72, 39, 4, 35]
print(maior_elemento(v))

print()

# 18 - Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por parâmetro
def preenche_lista(l):
    for i in range(10):
        l.append(i)
    return l

l = []
print(preenche_lista(l))

print()

# 19 - Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro.
#Para os próximos exercícios utilize estas lista para passar como parâmetro:
#Lista1 = [‘eds’, ‘56’, ‘fiap’, ‘ester’, ‘True’, ‘45.78’, ’12’, ’78’]
#Lista2 = [‘alberto’, ‘41’, ‘fiap’, ‘belem’, ‘False’, ‘70.780’, ’18’, ’171’]
def exibe_lista(l):
    for i in l:
        print(i)

Lista1 = ['eds', '56', 'fiap', 'ester', 'True', '45.78', '12', '78']
exibe_lista(Lista1)

print()

# 20 - Função ‘conta_elementos(l)’ que retorna a quantidade de elementos percorrendo a lista.
def conta_elementos(l):
    count = 0
    for i in l:
        count += 1
    def conta_elementos(l):
        count = 0
        for _ in l:
            count += 1
        return count

Lista1 = ['eds', '56', 'fiap', 'ester', 'True', '45.78', '12', '78']
print("Quantidade de elementos em Lista1:", conta_elementos(Lista1))

Lista2 = ['alberto', '41', 'fiap', 'belem', 'False', '70.780', '18', '171']
print("Quantidade de elementos em Lista2:", conta_elementos(Lista2))

# 21 - Retornar índice do elemento
def retorna_indice(elemento, l):
    for i in range(len(l)):
        if l[i] == elemento:
            return i
    return -1

Lista1 = ['eds', '56', 'fiap', 'ester', 'True', '45.78', '12', '78']

print("Índice de 'fiap' em Lista1:", retorna_indice('fiap', Lista1))
print("Índice de 'True' em Lista1:", retorna_indice('True', Lista1))
print("Índice de 'não existe' em Lista1:", retorna_indice('não existe', Lista1))

# 22 - quantidade de vezes que um elemento aparece em uma lista
def busca(l, elemento):
    count = 0
    for i in l:
        if i == elemento:
            count += 1
    return count

Lista1 = ['eds', '56', 'fiap', 'ester', 'True', '45.78', '12', '78', 'fiap']

print("Quantidade de 'fiap' em Lista1:", busca(Lista1, 'fiap'))
print("Quantidade de '56' em Lista1:", busca(Lista1, '56'))
print("Quantidade de 'não existe' em Lista1:", busca(Lista1, 'não existe'))

# 23 - Quantidade de inteiros na lista
def conta_inteiro(l):
    count = 0
    for i in l:
        if isinstance(i, int):
            count += 1
    return count

Lista1 = ['eds', 56, 'fiap', 'ester', True, 45.78, 12, '78']
Lista2 = [12, 34, 'texto', 56, 78, 90, '100']

print("Quantidade de inteiros em Lista1:", conta_inteiro(Lista1))
print("Quantidade de inteiros em Lista2:", conta_inteiro(Lista2))

# 24 - Quantidade de strings na lista
def conta_string(l):
    count = 0
    for i in l:
        if isinstance(i, str):
            count += 1
    return count

Lista1 = ['eds', 56, 'fiap', 'ester', True, 45.78, 12, '78']
Lista2 = [12, 34, 'texto', 56, 'palavra', 90, '100']

print("Quantidade de strings em Lista1:", conta_string(Lista1))
print("Quantidade de strings em Lista2:", conta_string(Lista2))

# 25 - quantidade de elementos booleanos
def conta_boolean(l):
    count = 0
    for i in l:
        if isinstance(i, bool):
            count += 1
    return count

Lista1 = ['eds', 56, 'fiap', 'ester', True, 45.78, 12, '78', False]
Lista2 = [12, 34, 'texto', 56, True, 90, False, '100']

print("Quantidade de booleanos em Lista1:", conta_boolean(Lista1))
print("Quantidade de booleanos em Lista2:", conta_boolean(Lista2))


# 26 - Quantidade de elementos floats
def conta_float(l):
    count = 0
    for i in l:
        if isinstance(i, float):
            count += 1
    return count

Lista1 = ['eds', 56, 'fiap', 'ester', True, 45.78, 12, '78']
Lista2 = [12, 34, 'texto', 56.7, 78, 90.5, '100']

print("Quantidade de floats em Lista1:", conta_float(Lista1))
print("Quantidade de floats em Lista2:", conta_float(Lista2))


# 27 - Copiar dados convertidos para inteiro
def copia_int(lista1, lista2):
    for item in lista1:
        try:
            numero = int(item)
            lista2.append(numero)
        except (ValueError, TypeError):
            pass

Lista1 = ['eds', '56', 'fiap', 'ester', True, '45.78', '12', '78']
Lista2 = []

copia_int(Lista1, Lista2)

print("Lista2 após copiar os inteiros de Lista1:", Lista2)