# cartão de crédito
def compra(conta, valor):
    conta['saldo'] += valor
    conta['transacoes'] += 1
    conta['media'] = conta['saldo'] / conta['transacoes']
    cashback = valor * 0.01
    conta['saldo'] -= cashback
    return conta

# Exemplo de uso
conta = {'saldo': 0, 'transacoes': 0, 'media': 0}
compra(conta, 200)
compra(conta, 300)
print(conta)
