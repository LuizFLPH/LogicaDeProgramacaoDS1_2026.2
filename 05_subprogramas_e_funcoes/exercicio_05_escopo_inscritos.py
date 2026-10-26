"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_de_inscritos = 0
def inscrever_aluno (quantidade):
    global total_de_inscritos
    total_de_inscritos = total_de_inscritos + quantidade
pass
quantidade = int(input("Quantos aluno foram escritos: "))
print("Antes: ", total_de_inscritos)
inscrever_aluno(quantidade)
print("Depois: ", total_de_inscritos)