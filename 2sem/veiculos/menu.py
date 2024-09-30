#### Fazendo o menu
#### AJUTES

from crud import *

while True:
    print ("Escolha as seguintes opções:\n1 - Incluir Veículo\n2 - Atualizar Veículo\n3 - Listar Veículos\n4 - Dar a saída de um veículo\n5 - Para sair do programa.")
    op = input ("Digite a sua opção:")
    match op:
        case "1":
            cliente = input ("Digite o nome do cliente:")
            modelo = input ("Digite o modelo do veículo:")
            ano = input ("Digite o ano do veículo:")
            placa = input ("Digite a placa do veículo:")
            problema = input ("Digite o problema do veículo:")
            print ("Selecione uma categoria:")
            print (categorias)
            categoria = input ("Digite o ID da categoria válido:")
            if categoria.isnumeric() and int(categoria) >= 0 and int(categoria) < len(categorias):
                print (create_car(cliente,modelo,ano,placa,problema,int(categoria)))
            else:
                print ("\n\nDigite uma categoria válida!!!\n\n")
                continue

        case "2":
            carros = read_car()
            for index,carro in enumerate(carros):
                print (f"{index}\t{carro["cliente"]}")
            indice_veiculo = input ("Qual veículo deseja atualizar:")
            if indice_veiculo.isnumeric() and int(indice_veiculo) >= 0 and int(indice_veiculo) < len(carros):
                cliente = input ("Digite o nome do cliente:")
                modelo = input ("Digite o modelo do veículo:")
                ano = input ("Digite o ano do veículo:")
                placa = input ("Digite a placa do veículo:")
                problema = input ("Digite o problema do veículo:")
                print ("Selecione uma categoria:")
                print (categorias)
                categoria = input ("Digite o ID da categoria válido:")
                if categoria.isnumeric() and int(categoria) >= 0 and int(categoria) < len(categorias):
                    print (update_car(int(indice_veiculo),cliente,modelo,ano,placa,problema,categoria))
                else:
                    print ("\n\nDigite uma categoria válida!!!\n\n")
                    continue
            else:
                print ("\n\nDigite um veículo válido!!!\n\n")
                continue
        case "3":
            carros = read_car()
            for carro in carros:
                for chave,valor in carro.items():
                    print (f"{chave}:{valor}")
                print ()
        case "4":
            carros = read_car()
            for index,carro in enumerate(carros):
                print (f"{index}\t{carro["cliente"]}")
            indice_veiculo = input ("Qual veículo deseja dar a saída:")
            if indice_veiculo.isnumeric() and int(indice_veiculo) >= 0 and int(indice_veiculo) < len(carros):
                desc_reparo_i = input ("Digite a descrição dos reparos:")
                print (update_car(int(indice_veiculo),desc_reparo=desc_reparo_i))
            else:
                print ("\n\nDigite um veículo válido!!!\n\n")
                continue
            
            
        case "5":
            break
        case _:
            ("\nDigite a sua opção válida!!!\n")

#from crud import *
#
#while True:
#    print ("Escolha as seguintes opções:\n1 - Incluir Veículo\n2 - Atualizar Veículo\n3 - Listar Veículos\n4 - Dar a saída de um veículo\n5 - Para sair do programa.")
#    op = input ("Digite a sua opção:")
#    match op:
#        case "1":
#            cliente = input ("Digite o nome do cliente:")
#            modelo = input ("Digite o modelo do veículo:")
#            ano = input ("Digite o ano do veículo:")
#            placa = input ("Digite a placa do veículo:")
#            problema = input ("Digite o problema do veículo:")
#            print ("Selecione uma categoria:")
#            print (categorias)
#            categoria = input ("Digite o ID da categoria válido:")
#            if categoria.isnumeric() and int(categoria) >= 0 and int(categoria) < len(categorias):
#                print (create_car(cliente,modelo,ano,placa,problema,int(categoria)))
#            else:
#                print ("\n\nDigite uma categoria válida!!!\n\n")
#                continue
#
#        case "2":
#            carros = read_car()
#            for index,carro in enumerate(carros):
#                print (f"{index}\t{carro["cliente"]}")
#            indice_veiculo = input ("Qual veículo deseja atualizar:")
#            if indice_veiculo.isnumeric() and int(indice_veiculo) >= 0 and int(indice_veiculo) < len(carros):
#                cliente = input ("Digite o nome do cliente:")
#                modelo = input ("Digite o modelo do veículo:")
#                ano = input ("Digite o ano do veículo:")
#                placa = input ("Digite a placa do veículo:")
#                problema = input ("Digite o problema do veículo:")
#                print ("Selecione uma categoria:")
#                print (categorias)
#                categoria = input ("Digite o ID da categoria válido:")
#                if categoria.isnumeric() and int(categoria) >= 0 and int(categoria) < len(categorias):
#                    print (update_car(int(indice_veiculo),cliente,modelo,ano,placa,problema,categoria))
#                else:
#                    print ("\n\nDigite uma categoria válida!!!\n\n")
#                    continue
#            else:
#                print ("\n\nDigite um veículo válido!!!\n\n")
#                continue
#        case "3":
#            carros = read_car()
#            for carro in carros:
#                for chave,valor in carro.items():
#                    print (f"{chave}:{valor}")
#                print ()
#        case "4":
#            carros = read_car()
#            for index,carro in enumerate(carros):
#                print (f"{index}\t{carro["cliente"]}")
#            indice_veiculo = input ("Qual veículo deseja dar a saída:")
#            if indice_veiculo.isnumeric() and int(indice_veiculo) >= 0 and int(indice_veiculo) < len(carros):
#                desc_reparo_i = input ("Digite a descrição dos reparos:")
#                print (update_car(int(indice_veiculo),desc_reparo=desc_reparo_i))
#            else:
#                print ("\n\nDigite um veículo válido!!!\n\n")
#                continue
#            
#            
#        case "5":
#            break
#        case _:
#            ("\nDigite a sua opção válida!!!\n")

