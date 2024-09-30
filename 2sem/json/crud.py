#### CRUD VEÍCULOS
import datetime as dt
import json

veiculos = []
categorias = ("1 - motor","2 - câmbio","3 - pneus","4 - freios","5 - suspenção","6- arrefecimento","7 - funilaria","8 - elétrico", "9 - tapeçaria","10 - revisão")

def create_car (cliente,modelo="vazio",ano="vazio", placa ="vazio",problema="vazio",categoria=-1):
    data = str(dt.datetime.now())
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

def update_car (indice, cliente="0",modelo="0",ano="0", placa = "0",problema="0",categoria=-1,desc_reparo="0"):
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

def save_to_json(file_path):
    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(veiculos, f, ensure_ascii=False, indent=4)