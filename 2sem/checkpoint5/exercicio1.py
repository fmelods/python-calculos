# Salvando em TXT
alunos = []

def incluir_alunos(nome, matricula, curso, turma, ano_ingresso):
    aluno = {
        "Nome": nome,
        "Matricula": matricula,
        "Curso": curso,
        "Turma": turma,
        "Ano de Ingresso": ano_ingresso
    }
    alunos.append(aluno)

def salvar_info(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f"Nome: {aluno['Nome']}\n")
            arquivo.write(f"Matricula: {aluno['Matricula']}\n")
            arquivo.write(f"Curso: {aluno['Curso']}\n")
            arquivo.write(f"Turma: {aluno['Turma']}\n")
            arquivo.write(f"Ano de Ingresso: {aluno['Ano de Ingresso']}\n")
            arquivo.write("\n")
    print(f"Informações dos alunos salvas em {nome_arquivo}")

if __name__ == "__main__":
    incluir_alunos("Felipe Melo", "556099", "ADS", "1TDSPW", 2024)
    incluir_alunos("Giovanna Menezes", "24158", "RH", "1RH", 2024)

    salvar_info("alunos.txt")
