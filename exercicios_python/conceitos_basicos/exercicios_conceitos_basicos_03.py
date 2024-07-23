quilometros= int(input('Quantos quitômetros foram percorridos? '))

'''def calc_metros():
    return quilometros * 1000

def calc_centimetros():
        return calc_metros() * 100

def calc_milimetros():
        return calc_centimetros() * 10'''

metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

    
print(f'Você percorreu um total de \n{metros} metros\n{centimetros} centimetros e \n{milimetros} milimetros.')