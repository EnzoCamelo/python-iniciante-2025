notas_alunos = {
    'Ana': [7.5, 8.0, 9.0],
    'Pedro': [6.0, 7.0, 6.5],
    'Maria': [9.0, 9.5, 8.5] 
}

for aluno, notas in notas_alunos.items():
    print(f'\nAluno: {aluno}')

    soma = sum(notas)
    qnt_notas = len(notas)

    if qnt_notas > 0:
        media = soma / qnt_notas
        print(f'Media final: {media:.2f}')

        if media >= 7.0:
            print('Aprovado!')
        else:
            print('Reprovado!')
    else:
        print('Não há notas cadastradas.')