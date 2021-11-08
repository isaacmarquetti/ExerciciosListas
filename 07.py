"""
Faça um Programa que leia um vetor de 5 números inteiros,
mostre a soma, a multiplicação e os números.
"""
from math import prod

soma = 0
mult = 0
numeros = []

for v in range(1, 6):
    numeros.append((int(input(f'Digite o {v}º número: '))))
    soma = sum(numeros)
    mult = prod(numeros)

print(f'A soma dos números: {soma}')
print(f'O produto dos números: {mult}')
print(f'Os números: {numeros}')


