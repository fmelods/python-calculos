import json

def ler_notas():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou deixe vazio para terminar): ")
        if nome == "":
            break
        nota1 = float(input(f"Digite a primeira nota de {nome}: "))
        nota2 = float(input(f"Digite a segunda nota de {nome}: "))
        alunos[nome] = (nota1, nota2)
    return alunos

def calcular_media(notas):
    return sum(notas) / len(notas)

def media_aluno(alunos, nome):
    if nome in alunos:
        return (nome, calcular_media(alunos[nome]))
    else:
        return (nome, None)

def aluno_maior_media(alunos):
    maior_media = -1
    aluno_com_maior_media = None
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        if media > maior_media:
            maior_media = media
            aluno_com_maior_media = nome
    return (aluno_com_maior_media, maior_media)

def salvar_em_json(alunos, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(alunos, f)

def carregar_de_json(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    arquivo = 'alunos.json'
    alunos = carregar_de_json(arquivo)
    novos_alunos = ler_notas()
    alunos.update(novos_alunos)
    salvar_em_json(alunos, arquivo)
    
    nome = input("Digite o nome do aluno para calcular a média: ")
    print(media_aluno(alunos, nome))
    
    print("Aluno com maior média:", aluno_maior_media(alunos))

main()