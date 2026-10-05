"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
X = int(input("Digite um numero"))
Y = int(input("Digite um numero"))
min = min(X, Y)
max = max(X, Y)

for i in range (min, max + 1):
    resto = i % 5
    if resto == 2 or resto == 3:
        print(i)