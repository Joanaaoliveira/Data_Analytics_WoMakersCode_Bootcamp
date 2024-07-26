
perguntas = ['Telefonou para a vítima? ', 
            'Esteve no local do crime? ',
            'Mora perto da vítima? ',
            'Devia para a vítima? ', 
            'Já trabalhou com a vítima?']

contagem = 0

for pergunta in perguntas:
    resposta = input(f'{pergunta} (Sim / Não): ').strip().upper()
    if resposta == 'SIM':
        contagem += 1
        
if contagem == 2:
    print('Você é considerado suspeito no crime!')
elif contagem == 3 or contagem == 4:
    print('Você é considerado cúmplice no crime!')
elif contagem == 5:
    print('Você é o assassino')
else:
    print('Você é inocente!')