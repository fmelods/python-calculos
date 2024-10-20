# carro de concessionária
from collections import defaultdict
from datetime import datetime

veiculos = []
categorias = defaultdict(int)

def registrar_entrada_veiculo():
    cliente = input("Nome do cliente: ")
    modelo = input("Modelo do veículo: ")
    ano = int(input("Ano do veículo: "))
    problema = input("Descrição do problema: ")
    
    print("Categorias disponíveis:")
    print("1. Motor\n2. Câmbio\n3. Pneus\n4. Freios\n5. Suspensão\n6. Arrefecimento\n7. Funilaria\n8. Elétrico\n9. Tapeçaria\n10. Revisão")
    categoria = int(input("Selecione a categoria do problema: "))
    
    categorias[categoria] += 1
    entrada = {
        'cliente': cliente,
        'modelo': modelo,
        'ano': ano,
        'problema': problema,
        'data_hora_entrada': datetime.now(),
        'categoria': categoria
    }
    veiculos.append(entrada)

def emitir_relatorio():
    print("\nRelatório de veículos por categoria de problema:")
    for categoria, quantidade in categorias.items():
        print(f"Categoria {categoria}: {quantidade} veículos")

def registrar_saida_veiculo():
    cliente = input("Nome do cliente para registrar a saída: ")
    servicos = input("Descrição dos serviços e peças trocadas: ")
    
    for veiculo in veiculos:
        if veiculo['cliente'] == cliente:
            veiculo['data_hora_saida'] = datetime.now()
            veiculo['servicos'] = servicos
            print(f"Saída registrada para o cliente {cliente}")
            return
    print("Veículo não encontrado.")

# Exemplo de uso
for _ in range(3):
    registrar_entrada_veiculo()

emitir_relatorio()
registrar_saida_veiculo()
