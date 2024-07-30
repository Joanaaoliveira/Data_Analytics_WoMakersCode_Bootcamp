numero_alunos = 5

qtd_notas = 4

medias = []

for i in range(numero_alunos):
    notas = []
    print(f'Aluno(a) {i + 1}: ')
    for j in range(qtd_notas):
        nota = float(input(f'Digite a nota {j + 1}: '))
        notas.append(nota)

    media = sum(notas) / qtd_notas
    medias.append(media)

alunos_acima_7 = len([media for media in medias if media >= 7.0])

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_7}")
