# chave valor
def encontrar_chaves_por_valor(dicionario, valor_buscado):
    chaves_encontradas = [chave for chave, valor in dicionario.items() if valor == valor_buscado]
    return chaves_encontradas

# Exemplo de uso
dicionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
valor = 1
print(encontrar_chaves_por_valor(dicionario, valor))
