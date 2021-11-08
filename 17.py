"""
Em uma competição de salto em distância cada atleta
tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois
informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado
o nome do atleta. A saída do programa deve ser conforme o
exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

tentativa = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
atletas = ''
dados = {}

while True:
    atletas = input('Digite o nome do atleta: ')
    if atletas == '':
        break
    saltos = []
    for v in tentativa:
        saltos.append(float(input(f'{v} salto: ')))
    dados[atletas] = saltos

soma = media = 0

for salto in saltos:
    soma += salto
media = soma / len(tentativa)

print("## RESULTADO FINAL ##")

for atletas, saltos in dados.items():
    print(f' Atleta: {atletas}')
    print(' Saltos: ', end='')
    print(' - '.join([str(salto) for salto in saltos]))
    print(f' Média dos saltos: {media:.1f}m')
    print()