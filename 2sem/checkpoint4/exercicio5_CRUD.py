
def create_aluno(curso, disciplina, turma, aluno, matricula, mensalidade):
    aluno = {
        "curso": curso,
        "disciplina": disciplina,
        "turma": turma,
        "aluno": aluno,
        "matricula": matricula,
        "mensalidade": mensalidade
    }

def read_aluno(aluno):
    print("Nome do curso:", aluno["curso"])
    print("Nome da disciplina:", aluno["disciplina"])
    print("Turma:", aluno["turma"])
    print("Nome do aluno:", aluno["aluno"])
    print("Registro de matricula:", aluno["matricula"])
    print("Valor da mensalidade:", aluno["mensalidade"])

def update_aluno(aluno, curso="Vazio", disciplina="Vazio", turma="Vazio", matricula="Vazio", mensalidade="Vazio"):
    if curso:
        aluno["curso"] = curso
    if disciplina:
        aluno["disciplina"] = disciplina
    if turma:
        aluno["turma"] = turma
    if matricula:
        aluno["matricula"] = matricula
    if mensalidade:
        aluno['mensalidade'] = mensalidade

def delete_aluno(alunos, aluno):
    for i in range(len(alunos)):
        if alunos[i]["aluno"] == aluno:
            del alunos[i]
            return True
    return False

def recalcular_mensalidade(alunos):
    for aluno in alunos:
        aluno['mensalidade'] *= 0.7
    print('Mensalidades recalculadas com desconto de 30%.')