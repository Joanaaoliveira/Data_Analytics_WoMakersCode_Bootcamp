# Exercícios Conceitos Básicos de Python
# 4) Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

combustivel = float(input('Qual foi a quantidade de litros de combustível consumidos? '))
distancia_percorrida = float(input('Qual foi a distância percorrida? '))

calcular_consumo = distancia_percorrida / combustivel

print(f'Você consumiu uma média de {calcular_consumo:.2f} km/l.')

