from exercicio5_CRUD import *

alunos = []

while True:
    print('Menu:')
    print('1. Criar Aluno')
    print('2. Atualizar Aluno')
    print('3. Recalcular Mensalidade')
    print('4. Sair')

    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        curso = input('Nome do curso: ')
        disciplina = input('Nome da disciplina: ')
        turma = input('Turma: ')
        aluno = input('Nome do aluno: ')
        matricula = input('Registro de matricula: ')
        mensalidade = float(input('Valor da mensalidade: '))

        create_aluno(curso, disciplina, turma, aluno, matricula, mensalidade)

    elif opcao == '2':
        matricula = input('Registro de matricula do aluno a ser atualizado: ')
        update_aluno(matricula)

    elif opcao == '3':
        recalcular_mensalidade(aluno)

    elif opcao == '4':
        break

    else:
        print('Opcao invalida. Tente novamente.')