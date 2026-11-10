"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
from ast import type_ignore


alunos = [
    [input("Insira o nome do aluno: ")], [float(input("Insira a primera nota do aluno: "))], [float(input("Insira a segunda nota do aluno: "))],
    [input("Insira o nome do aluno: ")], [float(input("Insira a primera nota do aluno: "))], [float(input("Insira a segunda nota do aluno: "))],
    [input("Insira o nome do aluno: ")], [float(input("Insira a primera nota do aluno: "))], [float(input("Insira a segunda nota do aluno: "))]
]
for linha in alunos:
    nome = alunos[0]
    nota1 = alunos[1]
    nota2 = alunos[2]
    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f"Parabens {nome} você esta aprovado!!, a sua média final foi de {media}")
    else:
        print(f"{nome} infelizmente você foi reprovado, estude mais da proxima!!")