# Exercícios Conceitos Básicos de Python
# 6) Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
#    IMC = peso / (altura x altura).

peso = float(input('Qual o seu peso em kgs? '))
altura = float(input('Qual sua altura em metros? '))

IMC = peso / (altura * altura)

def faixa_IMC(IMC):
    if IMC < 18.5:
        return 'abaixo do peso'
    elif IMC >= 18.5 and IMC <= 24.9:
        return 'no peso adequado'
    elif IMC >= 25 and IMC <= 29.9:
        return 'com sobrepeso'
    elif IMC >= 30 and IMC <= 34.9:
        return 'com obesidade grau 1'
    elif IMC >= 35 and IMC <= 39.9:
        return 'obesidade grau 2'
    else:
        return 'com obesidade extrema'


print(f'Seu IMC é {IMC:.2f}, de acordo com a tabelsa de classificação você está {faixa_IMC(IMC)}')