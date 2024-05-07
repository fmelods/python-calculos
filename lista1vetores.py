# 1 - 

# 2 - 

# 3 - 

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

# 15 - Fazer um procedimento chamado 'separa_pares_impares(v)' que coloque nas posições mais à esquerda os valores pares e mais a diretiaos impares
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

# 20