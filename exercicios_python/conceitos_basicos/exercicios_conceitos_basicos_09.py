# Exercícios Conceitos Básicos de Python
# 9) . Faça um Programa que utilize 4 variáveis como preferir e no final printuma mensagem 
# amigável utilizando as variáveis criadas

nome = input('Qual seu nome? ')
possui_carro = int(input('Você possui algum carro? (1-Sim, 2-Não)'))

if possui_carro == 1:
    marca = input('Qual a marca do seu carro?')
    modelo = input('Qual o modelo do seu carro? ')
    ano = int(input('Qual ano ele é? '))
    cor = input('Ele é de qual cor? ')
    print(f'Que legal {nome}, é um carro muito bonito o seu{marca} {modelo} {ano} na cor {cor}.')      
else:
    modelo = input('Se em breve você fosse comprar um, qual seria o modelo? ')
    cor = input('Qual cor? ')
    print(f'Interessante {nome}, espero que em breve você possa comprar o seu {modelo} {cor}')