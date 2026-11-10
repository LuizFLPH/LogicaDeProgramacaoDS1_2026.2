"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:
cidades = ("Tianguá", "São Benedito")
try:
    cidades[1] = "Ubajara"
except:
    print("Erro: O termo (Ubajara) não pode ser definido")
    print("Explicação: Uma tupla não pode ser alterada apos a sua criação")
    print("Solução: Insira o termo (Ubajara) dentro da tupla diretamente")
