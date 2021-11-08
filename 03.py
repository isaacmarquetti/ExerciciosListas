"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = []

for v in range(1, 5):
    notas.append(float(input(f"Informe a {v}ª nota: ")))

media = sum(notas) / 4

for v in range(0, 4):
    print(f'Nota {v+1}: {notas[v]}')

print(f'Média das notas: {media:.1f}')