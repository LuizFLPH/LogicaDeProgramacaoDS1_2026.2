"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("Digite a terceira nota "))
peso1 = 2
peso2 = 3
peso3 = 5
calc1 = nota1*peso1
calc2 = nota2*peso2
calc3 = nota3*peso3
media = (calc1+calc2+calc3)/(2+3+4)

print(f"A media do aluno sera: {media:.2f}")