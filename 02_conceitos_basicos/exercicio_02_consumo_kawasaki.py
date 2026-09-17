"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia = float(input("Distância percorrida"))
combustivel = float(input("Quantos litros de combustível sera ultilizado"))
consumo__medio = distancia/combustivel

print(f"Consumo médio da motocicleta sera: {consumo__medio:.2f} Km/L")
