# Exercícios Conceitos Básicos de Python
# 1) Um programa que peça dois números e realize as principais operações matemáticas.
import operator as op

def painel():
    print('\nQual operação matemática você gostaria de realizar?')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Divisão (resultado inteiro)')
    print('6 - Resto da divisão')
    print('7 - Sair do programa')

def main():
    while True:
        painel()
        opcao = input(('Escolha uma opção: '))
        if opcao == '1':
            soma()
        elif opcao == '2':
            subtracao()
        elif opcao == '3':
            multiplicacao()
        elif opcao == '4':
            divisao_1()
        elif opcao == '5':
            divisao_2()
        elif opcao == '6':
            divisao_3()
        elif opcao == '7':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida! Tente novamente.')
      

def soma():
    sum_01 = int(input('Digite o número 01: '))
    sum_02 = int(input('Digite o número 02: '))
    result_sum = op.add(sum_01,sum_02)
    print(f'O resultado é {result_sum}')

def subtracao():
    sub_01 = int(input('Digite o número 01: '))
    sub_02 = int(input('Digite o número 02: '))
    result_sub = op.sub(sub_01,sub_02)
    print(f'O resultado é {result_sub}')

def multiplicacao():
    multi_01 = int(input('Digite o número 01: '))
    multi_02 = int(input('Digite o número 02: '))
    result_mult = op.mul(multi_01,multi_02)
    print(f'O resultado é {result_mult}')

def divisao_1():
    div_01 = int(input('Digite o número 01: '))
    div_02 = int(input('Digite o número 02: '))
    result_div = op.truediv(div_01,div_02) # / - retorna o número float
    print(f'O resultado é {result_div:.2f}')

def divisao_2():
    div_01 = int(input('Digite o número 01: '))
    div_02 = int(input('Digite o número 02: '))
    result_div_int = op.floordiv(div_01,div_02) # // - retorna o número inteiro
    print(f'O resultado é {result_div_int}')

def divisao_3():
    div_01 = int(input('Digite o número 01: '))
    div_02 = int(input('Digite o número 02: '))
    result_rest_div = div_01%div_02
    print(f'O resultado é {result_rest_div}')

if __name__ == '__main__':
    main()
