"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
lista = ["Ryan Mesquita Damasceno"]
lista.append(input("Digite o nome de outro monitor"))
lista.append(input("Digite o nome de outro monitor"))
lista.insert(0, "Sophia Sousa Silva")
print(lista)