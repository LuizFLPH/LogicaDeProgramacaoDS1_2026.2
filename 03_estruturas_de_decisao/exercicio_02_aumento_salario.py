"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario =float(input("Insira seu salario: "))
if 0.00 < salario <= 400.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Seu novo salário sera R$ {novo_salario:.2f}, reajueste de {aumento:.2f}, ganho de 15%")
elif 400.01 < salario <= 800.00:
    aumento1 = salario * 0.12
    novo_salario1 = salario + aumento1
    print(f"Seu novo salário sera R$ {novo_salario1:.2f}, reajueste de {aumento1:.2f}, ganho de 12%")
elif 800.1 < salario <= 1200.00:
    aumento2 = salario * 0.10
    novo_salario2 = salario + aumento2
    print(f"Seu novo salário sera R$ {novo_salario2:.2f}, reajueste de {aumento2:.2f}, ganho de 10%")
elif 1200.01 < salario <= 2000.00:
    aumento3 = salario * 0.07
    novo_salario3 = salario+ aumento3
    print(f"Seu novo salário sera R$ {novo_salario3:.2f}, reajueste de {aumento3:.2f}, ganho de 7%")
elif salario > 2000.00:
    aumento4 = salario * 0.04
    novo_salario4 = salario + aumento4
    print(f"Seu novo salário sera R$ {novo_salario4:.2f}, reajueste de {aumento4:.2f}, ganho de 4%")