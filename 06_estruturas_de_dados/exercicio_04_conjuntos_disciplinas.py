"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web = {"João Enzo", "Witalo", "Davi", "Airley"}
alunos_banco = {"Davi", "João Pedro", "Emanuel", "Samuel"}

intersecao = alunos_web & alunos_banco
diferenca = alunos_web - alunos_banco
diferenca2 = alunos_banco - alunos_web

print(f"Os alunos que estão presentes nos 2 tipo de alunos são: {intersecao}")
print(f"Os alunos que estão presentes em apenas 1 dos tipos são: {diferenca},{diferenca2}")