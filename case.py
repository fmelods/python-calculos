votos_huguinho = 0
votos_zezinho = 0
votos_luizinho = 0
votos_nulos = 0
voto_invalido = 0
 
while True:
    voto = input("Insira o seu voto \n H/HUGUINHO\n Z/Zezinho\n L/Luizinho\n N/NULO\n S/SAIR")
 
    if voto == "S":
        break
 
    elif voto not in ["H" ,"Z" ,"L" ,"N"]:
        print("Voto Invallido")
        voto_invalido +=1
        continue
   
    match voto:
        case "H":
            print("Votou no Huguinho")
            votos_huguinho += 1
 
        case "Z":
            print("Votou no Zezinho")
            votos_zezinho += 1
       
        case "L":
            print("Votou no Luizinho")
            votos_luizinho += 1
 
        case "N":
            print("Votou Nulo")
            votos_nulos += 1
 
print("Resultado dos votos:")
print(f"Huguinho: {votos_huguinho}")
print(f"Zezinho:{votos_zezinho}")
print(f"Luizinho:{votos_luizinho}")
print(f"Votos Inválidos:{voto_invalido}")
print(f"Nulos:{votos_nulos}")