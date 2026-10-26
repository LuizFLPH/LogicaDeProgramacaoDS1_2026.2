"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo = distancia_km * (consumo_kml / preco_combustivel)
distancia_km = float(input("Digite a distância percorrida: "))
consumo_kml = float(input("Digite o consumo medio em Kml do veiculo: "))
preco_combustivel = float(input("Digite o preço em litros do combustivel: "))
calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)
pass
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo2 = qtd_pessoas * (dias * diaria_alimentacao)
qtd_pessoas = int(input("Digite o numero de pessoas: "))
dias = int(input("Digite o numero de dias: "))
diaria_alimentacao = int(input("Digite a diria de alimentação (em R%): "))
calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)
pass
custo = distancia_km * (consumo_kml / preco_combustivel)
custo2 = qtd_pessoas * (dias * diaria_alimentacao)
total = custo + custo2
print(f"O custo total da viagem foi de: {total:.2f}")