soma = 0
numero =int(input("Digite um numero:"))

while True:
    if numero != 0:
        print("Numero não foi encontrado")
    if numero == 0:
        print("A soma de todos os numero anteriores é :", soma)
        break
    soma += numero
    numero = int(input("Digite outro numero:"))