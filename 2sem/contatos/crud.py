#CRUD - VERSÃO 2
contatos = []
def create (nome,nome_completo="vazio",telefone="vazio",celular="vazio"):
    if len(contatos) < 20:
        contato = {
               "nome":nome,
               "nome_completo":nome_completo,
                "telefone":telefone,
                "celular":celular
            }
        contatos.append(contato)
        return len(contatos)
    else:
        return -1

def read(indice=-1):
    if indice >-1 and indice < len(contatos):
        return contatos[indice]
    else:
        return contatos

def update (indice, nome="0", nome_completo="0",telefone="0",celular="0"):
    if indice < len(contatos):
        if nome!="0":
            contatos[indice].update({"nome":nome})
        if nome_completo!="0":
            contatos[indice].update({"nome_completo":nome_completo})
        if telefone!="0":
            contatos[indice].update({"telefone":telefone})
        if celular!="0":
            contatos[indice].update({"celular":celular})
        return True
    else:
        return False
    
def delete (indice):
    if indice < len(contatos):
        contatos.pop(indice)
        return True
    else:
        return False
    
def exibir():
    if len(contatos) == 0:
        print("Nenhum contato cadastrado.")
    else:
        contatos_ordenados = sorted(contatos, key=lambda contato: contato["nome"].lower())
        
        for contato in contatos_ordenados:
            print(f"Nome: {contato['nome']}, Nome Completo: {contato['nome_completo']}, Telefone: {contato['telefone']}, Celular: {contato['celular']}")

#CRUD - EXERCÍCIO DE CONTATOS PRIORITÁRIOS
#contatos = []
#def create (nome,nome_completo="vazio",telefone="vazio",celular="vazio"):
#    if len(contatos) < 20:
#        contato = {
#               "nome":nome,
#               "nome_completo":nome_completo,
#                "telefone":telefone,
#                "celular":celular
#            }
#        contatos.append(contato)
#        return len(contatos)
#    else:
#        return -1
#
#def read(indice=-1):
#    if indice >-1 and indice < len(contatos):
#        return contatos[indice]
#    else:
#        return contatos
#
#def update (indice, nome="0", nome_completo="0",telefone="0",celular="0"):
#    if indice < len(contatos):
#        if nome!="0":
#            contatos[indice].update({"nome":nome})
#        if nome_completo!="0":
#            contatos[indice].update({"nome_completo":nome_completo})
#        if telefone!="0":
#            contatos[indice].update({"telefone":telefone})
#        if celular!="0":
#            contatos[indice].update({"celular":celular})
#        return True
#    else:
#        return False
#    
#def delete (indice):
#    if indice < len(contatos):
#        contatos.pop(indice)
#        return True
#    else:
#        return False

#CRUD NOVO (FEITO COM DICIONÁRIOS)
#contatos = []
#def create (nome,nome_completo="vazio",telefone="vazio",celular="vazio"):
#    if len(contatos) < 20:
#        contato = {
#               "nome":nome,
#               "nome_completo":nome_completo,
#                "telefone":telefone,
#                "celular":celular
#            }
#        contatos.append(contato)
#        return len(contatos)
#    else:
#        return -1
#
#def read(indice=-1):
#    if indice >-1 and indice < len(contatos):
#        return contatos[indice]
#    else:
#        return contatos
#
#def update (indice, nome="0", nome_completo="0",telefone="0",celular="0"):
#    if indice < len(contatos):
#        if nome!="0":
#            contatos[indice].update({"nome":nome})
#        if nome_completo!="0":
#            contatos[indice].update({"nome_completo":nome_completo})
#        if telefone!="0":
#            contatos[indice].update({"telefone":telefone})
#        if celular!="0":
#            contatos[indice].update({"celular":celular})
#        return True
#    else:
#        return False
#    
#def delete (indice):
#    if indice < len(contatos):
#        contatos.pop(indice)
#        return True
#    else:
#        return False
            

#CRUD ANTIGO (FEITO COM VETORES E NÃO COM DICIONÁRIOS)
#contatos = []
#
#def create (nome,nome_completo="vazio",telefone="vazio",celular="vazio"):
#    if len(contatos) < 20:
#        contatos.append([nome,nome_completo,telefone,celular])
#        return len(contatos)
#    else:
#        return -1
# 
#def read(indice=-1):
#    if indice >-1 and indice < len(contatos):
#        return contatos[indice]
#    else:
#        return contatos
# 
#def update (indice, nome="0", nome_completo="0",telefone="0",celular="0"):
#    if indice < len(contatos):
#        if nome!="0":
#            contatos[indice][0]=nome
#        if nome_completo!="0":
#            contatos[indice][1]=nome_completo
#        if telefone!="0":
#            contatos[indice][2]=telefone
#        if celular!="0":
#            contatos[indice][3]=celular
#        return True
#    else:
#        return False
#
#def delete (indice):
#    if indice < len(contatos):
#        contatos.pop(indice)
#        return True
#    else:
#        return False