"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total(fase1, fase2, fase3):
    pontuacao = fase1 + fase2 + fase3
    print(f"A pontuação total da equipe é:{pontuacao}")
fase1 = int(input("Pontuação da fase 1: "))
fase2 = int(input("Pontuação da fase 2: "))
fase3 = int(input("Pontuação da fase 3: "))
calcular_pontuacao_total(fase1, fase2, fase3)