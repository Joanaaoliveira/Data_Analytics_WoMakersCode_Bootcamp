# Exercícios Conceitos Básicos de Python

horas_exercicio_fisico = float(input('Quantas horas você pratica exercicio físico por semana? '))

def calculo_calorias():
    media_calorias = 5
    horas_minutos = (horas_exercicio_fisico * 60) * media_calorias
    return horas_minutos

print(f'Mantendo o tempo de {horas_exercicio_fisico} horas por semana, você queimará '
      f'{calculo_calorias():.2f} calorias por mês')