#### CRUD VEÍCULOS
#### VERSÃO 5
import datetime as dt
veiculos = []
categorias = ("motor","câmbio","pneus","freios","suspenção","arrefecimento","funilaria","elétrico", "tapeçaria","revisão")

def create_car (cliente,modelo="vazio",ano="vazio", placa ="vazio",problema="vazio",categoria=-1):
    data = dt.datetime.now()
    veiculo = {
        "cliente":cliente,
        "data":data,
        "modelo":modelo,
        "ano":ano,
        "placa":placa,
        "problema":problema,
        "categoria":categoria
    }
    veiculos.append(veiculo)
    return len(veiculos)
    
def read_car(indice=-1):
    if indice >-1 and indice < len(veiculos):
        return veiculos[indice]
    else:
        return veiculos

def update_car (indice, cliente="vazio",modelo="vazio",ano="vazio", placa = "vazio",problema="vazio",categoria=-1,desc_reparo="vazio"):
    if indice < len(veiculos):
        if cliente!="0":
            veiculos[indice].update({"cliente":cliente})
        if modelo!="0":
            veiculos[indice].update({"modelo":modelo})
        if ano!="0":
            veiculos[indice].update({"ano":ano})
        if placa!="0":
            veiculos[indice].update({"placa":placa})
        if problema!="0":
            veiculos[indice].update({"problema":problema})
        if categoria!="0":
            veiculos[indice].update({"categoria":categoria})
        if desc_reparo !="0":
            veiculos[indice]["desc_reparo"]=desc_reparo
            veiculos[indice]["data_saida"] = dt.datetime.now()
        return True
    else:
        return False
    
def delete_car (indice):
    if indice < len(veiculos):
        veiculos.pop(indice)
        return True
    else:
        return False


#### VERSÃO 4
#veiculos = []
#def create_car (proprietario,combustivel="vazio",modelo="vazio",cor="vazio", ano="vazio", placa = "vazio"):
#    if len(veiculos) < 20:
#        veiculo = {
#               "proprietario":proprietario,
#               "combustivel":combustivel,
#                "modelo":modelo,
#                "cor":cor,
#                "ano":ano,
#                "placa":placa
#            }
#        veiculos.append(veiculo)
#        return len(veiculos)
#    else:
#        return -1
#
#def read_car(indice=-1):
#    if indice >-1 and indice < len(veiculos):
#        return veiculos[indice]
#    else:
#        return veiculos
#
#def update_car (indice, proprietario="0",combustivel="0",modelo="0",cor="0", ano="0", placa = "0"):
#    if indice < len(veiculos):
#        if proprietario!="0":
#            veiculos[indice].update({"proprietario":proprietario})
#        if combustivel!="0":
#            veiculos[indice].update({"combustivel":combustivel})
#        if modelo!="0":
#            veiculos[indice].update({"modelo":modelo})
#        if cor!="0":
#            veiculos[indice].update({"cor":cor})
#        if ano!="0":
#            veiculos[indice].update({"ano":ano})
#        if placa!="0":
#            veiculos[indice].update({"placa":placa})
#        return True
#    else:
#        return False
#    
#def delete_car (indice):
#    if indice < len(veiculos):
#        veiculos.pop(indice)
#        return True
#    else:
#        return False


#### VERSÃO 3
#import datetime as dt
#veiculos = []
#categorias = ("1 - motor","2 - câmbio","3 - pneus","4 - freios","5 - suspenção","6- arrefecimento","7 - funilaria","8 - elétrico", "9 - tapeçaria","10 - revisão")
#
#def create_car (cliente,modelo="vazio",ano="vazio", placa ="vazio",problema="vazio",categoria=-1):
#    data = dt.datetime.now()
#    veiculo = {
#        "cliente":cliente,
#        "data":data,
#        "modelo":modelo,
#        "ano":ano,
#        "placa":placa,
#        "problema":problema,
#        "categoria":categoria
#    }
#    veiculos.append(veiculo)
#    return len(veiculos)
#    
#def read_car(indice=-1):
#    if indice >-1 and indice < len(veiculos):
#        return veiculos[indice]
#    else:
#        return veiculos
#
#def update_car (indice, cliente="0",modelo="0",ano="0", placa = "0",problema="0",categoria=-1,desc_reparo="0"):
#    if indice < len(veiculos):
#        if cliente!="0":
#            veiculos[indice].update({"cliente":cliente})
#        if modelo!="0":
#            veiculos[indice].update({"modelo":modelo})
#        if ano!="0":
#            veiculos[indice].update({"ano":ano})
#        if placa!="0":
#            veiculos[indice].update({"placa":placa})
#        if problema!="0":
#            veiculos[indice].update({"problema":problema})
#        if categoria!="0":
#            veiculos[indice].update({"categoria":categoria})
#        if desc_reparo !="0":
#            veiculos[indice]["desc_reparo"]=desc_reparo
#            veiculos[indice]["data_saida"] = dt.datetime.now()
#        return True
#    else:
#        return False
#    
#def delete_car (indice):
#    if indice < len(veiculos):
#        veiculos.pop(indice)
#        return True
#    else:
#        return False


#### VERSÃO 2
#veiculos = []
#def create_car (proprietario,combustivel="vazio",modelo="vazio",cor="vazio", ano="vazio", placa = "vazio"):
#    if len(veiculos) < 20:
#        veiculo = {
#               "proprietario":proprietario,
#               "combustivel":combustivel,
#                "modelo":modelo,
#                "cor":cor,
#                "ano":ano,
#                "placa":placa
#            }
#        veiculos.append(veiculo)
#        return len(veiculos)
#    else:
#        return -1
#
#def read_car(indice=-1):
#    if indice >-1 and indice < len(veiculos):
#        return veiculos[indice]
#    else:
#        return veiculos
#
#def update_car (indice, proprietario="0",combustivel="0",modelo="0",cor="0", ano="0", placa = "0"):
#    if indice < len(veiculos):
#        if proprietario!="0":
#            veiculos[indice].update({"proprietario":proprietario})
#        if combustivel!="0":
#            veiculos[indice].update({"combustivel":combustivel})
#        if modelo!="0":
#            veiculos[indice].update({"modelo":modelo})
#        if cor!="0":
#            veiculos[indice].update({"cor":cor})
#        if ano!="0":
#            veiculos[indice].update({"ano":ano})
#        if placa!="0":
#            veiculos[indice].update({"placa":placa})
#        return True
#    else:
#        return False
#    
#def delete_car (indice):
#    if indice < len(veiculos):
#        veiculos.pop(indice)
#        return True
#    else:
#        return False


#CRUD NOVO (FEITO COM DICIONÁRIOS)
#veiculos = []
#def create_car (proprietario,combustivel="vazio",modelo="vazio",cor="vazio", ano="vazio", placa = "vazio"):
#    if len(veiculos) < 20:
#        veiculo = {
#               "proprietario":proprietario,
#               "combustivel":combustivel,
#                "modelo":modelo,
#                "cor":cor,
#                "ano":ano,
#                "placa":placa
#            }
#        veiculos.append(veiculo)
#        return len(veiculos)
#    else:
#        return -1
# 
#def read_car(indice=-1):
#    if indice >-1 and indice < len(veiculos):
#        return veiculos[indice]
#    else:
#        return veiculos
# 
#def update_car (indice, proprietario="0",combustivel="0",modelo="0",cor="0", ano="0", placa = "0"):
#    if indice < len(veiculos):
#        if proprietario!="0":
#            veiculos[indice].update({"proprietario":proprietario})
#        if combustivel!="0":
#            veiculos[indice].update({"combustivel":combustivel})
#        if modelo!="0":
#            veiculos[indice].update({"modelo":modelo})
#        if cor!="0":
#            veiculos[indice].update({"cor":cor})
#        if ano!="0":
#            veiculos[indice].update({"ano":ano})
#        if placa!="0":
#            veiculos[indice].update({"placa":placa})
#        return True
#    else:
#        return False
#   
#def delete_car (indice):
#    if indice < len(veiculos):
#        veiculos.pop(indice)
#        return True
#    else:
#        return False

#CRUD ANTIGO (FEITO COM VETORES E NÃO COM DICIONÁRIOS)
#veiculos = []
#
#def create_car (proprietario,combustivel="vazio",modelo="vazio",cor="vazio", ano="vazio", placa = "vazio"):
#    if len(veiculos) < 20:
#        veiculos.append([proprietario,combustivel,modelo,cor,ano,placa])
#        return len(veiculos)
#    else:
#        return -1
# 
#def read_car(indice=-1):
#    if indice >-1 and indice < len(veiculos):
#        return veiculos[indice]
#    else:
#        return veiculos
# 
#def update_car (indice, proprietario="0",combustivel="0",modelo="0",cor="0", ano="0", placa = "0"):
#    if indice < len(veiculos):
#        if proprietario!="0":
#            veiculos[indice][0]=proprietario
#        if combustivel!="0":
#            veiculos[indice][1]=combustivel
#        if modelo!="0":
#            veiculos[indice][2]=modelo
#        if cor!="0":
#            veiculos[indice][3]=cor
#        if ano!="0":
#            veiculos[indice][4]=ano
#        if placa!="0":
#            veiculos[indice][5]=placa
#        return True
#    else:
#        return False
#
#def delete_car (indice):
#    if indice < len(veiculos):
#        veiculos.pop(indice)
#        return True
#    else:
#        return False
#
#print(create_car("Alberto"))
#print (read_car())
#print (update_car(1,proprietario="Alberto Messias",combustivel="flex",modelo="SPIN",cor="PRATA", ano="2020", placa = "DSK2A89"))
 