import json

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def gerar_relatorio(votos):
    resumo_candidatos = {}
    
    for voto in votos:
        candidato = voto['candidato']
        if candidato not in resumo_candidatos:
            resumo_candidatos[candidato] = 0
        resumo_candidatos[candidato] += 1
    
    return resumo_candidatos

def exibir_relatorio(resumo_candidatos):
    print("Relatório de Votos:")
    for candidato, votos in resumo_candidatos.items():
        print(f"Candidato: {candidato}, Votos: {votos}")

def main():
    caminho_arquivo = 'C:\Users\Thanatos\Documents\listaEntrega\auditoria_votos.json'  
    votos = ler_arquivo_json(caminho_arquivo)
    resumo_candidatos = gerar_relatorio(votos)
    exibir_relatorio(resumo_candidatos)

main()