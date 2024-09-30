import json
from datetime import datetime

# Inicialização das variáveis
votos = {'H': 0, 'Z': 0, 'L': 0, 'N': 0}
votos_invalidos = 0
auditoria = []

def salvar_auditoria():
    with open(r'C:\Users\Thanatos\Documents\listaEntrega\auditoria_votos.json', 'w') as f:
        json.dump(auditoria, f, indent=4)

def exibir_resultados():
    print("\nResultados da votação:")
    print(f"Huguinho: {votos['H']} votos")
    print(f"Zezinho: {votos['Z']} votos")
    print(f"Luizinho: {votos['L']} votos")
    print(f"Votos nulos: {votos['N']} votos")
    print(f"Votos inválidos: {votos_invalidos} votos")

    vencedor = max(votos, key=votos.get)
    if votos[vencedor] == 0 or list(votos.values()).count(votos[vencedor]) > 1:
        print("Não houve vencedor.")
    else:
        print(f"O vencedor é: {vencedor}")

def exibir_auditoria():
    print("\nRelatório de auditoria:")
    for registro in auditoria:
        print(f"ID: {registro['id']}, Voto: {registro['voto']}, Data/Hora: {registro['timestamp']}")

def main():
    global votos_invalidos
    contador_id = 1

    while True:
        print("\nMenu de votação:")
        print("H - Votar em Huguinho")
        print("Z - Votar em Zezinho")
        print("L - Votar em Luizinho")
        print("N - Votar nulo")
        print("S - Terminar a votação")
        print("A - Exibir relatório de auditoria")

        escolha = input("Escolha uma opção: ").upper()

        if escolha in ['H', 'Z', 'L', 'N']:
            votos[escolha] += 1
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            auditoria.append({'id': contador_id, 'voto': escolha, 'timestamp': timestamp})
            contador_id += 1
        elif escolha == 'S':
            exibir_resultados()
            salvar_auditoria()
            break
        elif escolha == 'A':
            exibir_auditoria()
        else:
            votos_invalidos += 1
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            auditoria.append({'id': contador_id, 'voto': 'Inválido', 'timestamp': timestamp})
            contador_id += 1
            print("Voto inválido. Tente novamente.")

main()