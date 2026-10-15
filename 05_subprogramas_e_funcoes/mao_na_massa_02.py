# TODO: Crie a função lambda aqui
calcular_acrescimo = lambda c : c*(10/100) + c


# Teste
c = int(input("Digite um numero: "))
acrescimo = calcular_acrescimo(c)
print(acrescimo)