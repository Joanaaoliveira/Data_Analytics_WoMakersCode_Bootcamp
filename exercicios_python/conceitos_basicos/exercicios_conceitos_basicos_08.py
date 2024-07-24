# Exercícios Conceitos Básicos de Python
# 6) Solicite ao usuário o número de horas de exercício físico por semana.Calcule o total de 
# calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas_exercicio_fisico = float(input('Quantas horas você pratica exercicio físico por semana? '))

def calculo_calorias():
    media_calorias = 5
    horas_minutos = (horas_exercicio_fisico * 60) * media_calorias
    return horas_minutos

print(f'Mantendo o tempo de {horas_exercicio_fisico} horas por semana, você queimará '
      f'{calculo_calorias():.2f} calorias por mês')