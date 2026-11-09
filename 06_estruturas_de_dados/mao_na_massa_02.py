# TODO: Crie a matriz 2x2 e calcule a soma
matriz = [
    [int(input()), int(input())],
    [int(input()), int(input())]
]

# Escreva a lógica de soma aqui
print("O valor da soma é de:")
for linha in matriz:
    n1 = linha[0]
    n2 = linha[1]
    soma = n1 + n2
    print(f"{n1}+{n2}={soma}")