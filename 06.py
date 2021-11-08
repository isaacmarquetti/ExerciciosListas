"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

boletim = []

for i in range(0, 3):
    notas = []
    print(f'Aluno #{i+1}#:')
    for j in range(0, 4):
        notas.append(float(input(f' Nota {j+1}: ')))
    boletim.append(notas)

aprovados = somar = 0

for notas in boletim:
    somar = sum(notas)
    if somar / 4 >= 7:
        aprovados += 1

print(f'Alunos com média >= 7.0: {aprovados} alunos.')
