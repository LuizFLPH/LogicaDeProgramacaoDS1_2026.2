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
aluno = []
for i in range (0,3):
    nome = str(input("Insira o nome do aluno: "))
    nota1 = float(input("Insira a primeira nota do aluno: "))
    nota2 = float(input("Insira a segunda nota do aluno: "))

    aluno.append([nome, nota1, nota2])

for linha in aluno:
    nome = linha[0]
    nota1 = linha[1]
    nota2 = linha[2]
    media = (nota1 + nota2) / 2
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado" 
    print(f"Aluno: {nome} | Média: {media} | Situação: {situacao} / Prova Final")