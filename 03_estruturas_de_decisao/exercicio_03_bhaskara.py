"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
A = float(input("Valor do A "))
B = float(input("Valor do B "))
C = float(input("Valor do C "))
Delta = (B**2)-(4*A*C)
if Delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    X1 = (-B + Delta**0.5) / (2 * A)
    X2 = (-B - Delta**0.5) / (2 * A)
    print(f"X1 = {X1:.5f}, X2 = {X2:.5f}")