"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade =  int(input("Insira sua idade"))
if idade > 12 and idade < 60:
    print("Você esta na faxetaria Integral, o valor do seu ingresso é 100 R$")
elif idade <= 12:
    print("Você estan na faxetaria Infantil, o valor do seu ingresso é de 50 R$")
elif idade >= 60:
    print("Você esta na faxetaria Melhor Idade, o valor do seu ingresso e Gratuito")
else:
    print("Valor não encontrado")