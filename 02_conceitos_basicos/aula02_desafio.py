# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
valor_conta = float (input("Valor a pagar: "))
numero_pessoas = float (input("Numero total de pessoas: "))
valor_total = valor_conta / numero_pessoas
print(f"O valor a pagar para cada pessoas sera: {valor_total:.2f}")


