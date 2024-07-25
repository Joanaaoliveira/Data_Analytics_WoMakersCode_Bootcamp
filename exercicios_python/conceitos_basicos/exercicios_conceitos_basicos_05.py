# Exercícios Conceitos Básicos de Python

distancia_viagem = int(input('Quantos quilometros separam você do seu destino? '))

def equivalencia_aviao():
    velocidade_aviao = 600
    calc_equiv_aviao = distancia_viagem / velocidade_aviao
    if calc_equiv_aviao < 1:
        calc_equiv_aviao *= 60
        validacao_aviao = 'minutos'
        horas = int(calc_equiv_aviao // 60)
        minutos = int(calc_equiv_aviao % 60)
        return f'{horas} horas e {minutos} minutos'
    else:
        validacao_aviao = 'horas'
        horas = int(calc_equiv_aviao)
        minutos = int((calc_equiv_aviao - horas) * 60)
        return f'{horas} horas e {minutos} minutos'

def equivalencia_carro():
    velocidade_carro = 100
    calc_equiv_carro = distancia_viagem / velocidade_carro
    if calc_equiv_carro < 1:
        calc_equiv_carro *= 60
        validacao_carro = 'minutos'
        horas = int(calc_equiv_carro // 60)
        minutos = int(calc_equiv_carro % 60)
        return f'{horas} horas e {minutos} minutos'
    else:
        validacao_carro = 'horas'
        horas = int(calc_equiv_carro)
        minutos = int((calc_equiv_carro - horas) * 60)
        return f'{horas} horas e {minutos} minutos'

def equivalencia_onibus():
    velocidade_onibus = 80
    calc_equiv_onibus = distancia_viagem / velocidade_onibus
    if calc_equiv_onibus < 1:
        calc_equiv_onibus *= 60
        validacao_onibus = 'minutos'
        horas = int(calc_equiv_onibus // 60)
        minutos = int(calc_equiv_onibus % 60)
        return f'{horas} horas e {minutos} minutos'
    else:
        validacao_onibus = 'horas'
        horas = int(calc_equiv_onibus)
        minutos = int((calc_equiv_onibus - horas) * 60)
        return f'{horas} horas e {minutos} minutos'

tempo_aviao = equivalencia_aviao()
tempo_carro = equivalencia_carro()
tempo_onibus = equivalencia_onibus()

print(f'Você gastaria para chegar ao seu destino \n{tempo_aviao} de avião.\n'
      f'{tempo_carro} de carro e \n{tempo_onibus} de ônibus')
