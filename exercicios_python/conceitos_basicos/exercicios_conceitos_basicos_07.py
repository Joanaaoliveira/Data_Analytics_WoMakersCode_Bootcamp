# Exercícios Conceitos Básicos de Python
# 6) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês.Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Quantos você ganha por hora trabalhada?'))
horas_trabalhadas = float(input('Quantas horas você trabalhou neste mês? '))

calculo_salario = valor_hora * horas_trabalhadas

print(f'Você receberá neste mês {calculo_salario} reais')