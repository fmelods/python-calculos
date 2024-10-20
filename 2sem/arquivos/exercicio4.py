# notas dos alunos
def media_aluno(dicionario, nome_aluno):
    notas = dicionario.get(nome_aluno, [])
    if notas:
        return sum(notas) / len(notas)
    return None

def aluno_com_maior_media(dicionario):
    maior_media = -1
    aluno_top = ''
    for aluno, notas in dicionario.items():
        media = sum(notas) / len(notas)
        if media > maior_media:
            maior_media = media
            aluno_top = aluno
    return aluno_top, maior_media

alunos = {}
while True:
    nome = input("Digite o nome do aluno (ou vazio para encerrar): ")
    if nome == '':
        break
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    alunos[nome] = (nota1, nota2)

# Exemplo de uso
nome_aluno = input("Digite o nome do aluno para ver a média: ")
print(f"Média do aluno {nome_aluno}: {media_aluno(alunos, nome_aluno)}")
aluno_top, maior_media = aluno_com_maior_media(alunos)
print(f"Aluno com maior média: {aluno_top}, média: {maior_media}")
