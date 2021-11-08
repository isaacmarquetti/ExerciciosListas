"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos.
"""

alunos = []

for v in range(1, 3):
    aluno = []
    print(f'Aluno {v} - Informe a idade e altura:')
    aluno.append(int(input(" Idade: ")))
    aluno.append(float(input(" Altura(m): ")))
    alunos.append(aluno)

soma_altura = media_altura = cont_baixo = cont = 0

for aluno in alunos:
    soma_altura += aluno[1]
    cont += 1

media_altura = soma_altura / cont

for aluno in alunos:
    if aluno[0] >= 13 and aluno[1] <= media_altura:
        cont_baixo += 1

print(f'Alunos com mais de 13 anos e altura inferior a média: {cont_baixo}')
