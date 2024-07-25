# Exercícios Conceitos Básicos de Python

from datetime import date

def calcula_idade():
    dia_nascimento = int(input('Qual o dia do seu nascimento? '))
    mes_nascimento = int(input('Qual o mês do seu nascimento? '))
    ano_nascimento = int(input('Qual o ano do seu nascimento? '))

    
    data_atual = date.today()
    
    idade = data_atual.year - ano_nascimento
    
    if (data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento):
        idade -= 1
    
    return idade

print(f'Você tem {calcula_idade()} anos.')
