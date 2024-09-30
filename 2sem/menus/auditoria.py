# votação com auditoria
import time
from collections import defaultdict

votos = defaultdict(int)
audit_trail = []

def votar(candidato):
    voto_id = len(audit_trail) + 1
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    audit_trail.append({'id': voto_id, 'candidato': candidato, 'data_hora': timestamp})
    votos[candidato] += 1

def exibir_auditoria():
    print("\nRelatório Auditável de Votos")
    for registro in audit_trail:
        print(f"ID: {registro['id']}, Candidato: {registro['candidato']}, Data/Hora: {registro['data_hora']}")

def exibir_resultados():
    print("\nResultados da Votação")
    print(f"Huguinho: {votos['H']}")
    print(f"Zezinho: {votos['Z']}")
    print(f"Luizinho: {votos['L']}")
    print(f"Nulos: {votos['N']}")
    print(f"Votos Inválidos: {votos['Invalido']}")
    
    total_votos_validos = votos['H'] + votos['Z'] + votos['L']
    if total_votos_validos == 0:
        print("Nenhum voto válido registrado.")
    else:
        vencedor = max(votos, key=lambda k: votos[k] if k in ['H', 'Z', 'L'] else 0)
        print(f"O vencedor é: {vencedor}")

while True:
    print("\nMenu de Votação: ")
    print("H - Huguinho | Z - Zezinho | L - Luizinho | N - Nulo | S - Sair")
    print("A - Exibir relatório auditável")
    opcao = input("Escolha uma opção: ").upper()

    if opcao in ['H', 'Z', 'L', 'N']:
        votar(opcao)
    elif opcao == 'S':
        exibir_resultados()
        break
    elif opcao == 'A':
        exibir_auditoria()
    else:
        print("Opção inválida. Tente novamente.")
        votar('Invalido')
