def incluir_informacoes(lista_alunos, nome, matricula, curso, turma, ano):
    aluno = {
        'Nome': nome,
        'Matricula': matricula,
        'Curso': curso,
        'Turma': turma,
        'Ano de Ingresso': ano
    }
    lista_alunos.append(aluno)

def exibir_informacoes(lista_alunos):
    for aluno in lista_alunos:
        print('Nome:', aluno['Nome'])
        print('Matricula:', aluno['Matricula'])
        print('Curso:', aluno['Curso'])
        print('Turma:', aluno['Turma'])
        print('Ano de Ingresso:', aluno['Ano de Ingresso'])

lista_alunos = []
incluir_informacoes(lista_alunos, 'Felipe Melo', 'RM556099', 'ADS', '1TDSPW', '2023')
exibir_informacoes(lista_alunos)