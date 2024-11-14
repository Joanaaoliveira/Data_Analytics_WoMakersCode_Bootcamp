## O programa abaixo deve calcular a média digitada pelo usuário;
# No entanto, ele não está funcionando bem. Você pode concertá-lo?

valores = []
continuar = True

def calcular_media(valores):
    tamanho = len(valores)
    if tamanho == 0:
        return 0
    soma = sum(valores)
    media = soma / tamanho
    return media



while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False  # primeiro erro, false estava 'false' - modificado para False
    else: 
        try:
            numero = float(valor)
            valores.append(numero)
        except ValueError:
            print("Por favor, digite um número válido ou 'ok' para finalizar.")



media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media}')