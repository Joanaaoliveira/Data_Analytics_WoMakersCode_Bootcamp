# Exercícios Conceitos Básicos de Python
# 2) Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
from datetime import date

def calcula_idade():
    ano_nascimento = int(input('Qual o ano do seu nascimento? '))
    mes_nascimento = int(input('Qual o mês do seu nascimento? '))
    dia_nascimento = int(input('Qual o dia do seu nascimento? '))
    
    data_atual = date.today()
    
    idade = data_atual.year - ano_nascimento
    
    if (data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento):
        idade -= 1
    
    return idade

print(f'Você tem {calcula_idade()} anos.')
