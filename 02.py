"""
Faça um Programa que leia um vetor de 10 números reais
e mostre-os na ordem inversa.
"""
num = []

for v in range(1, 11):
    num.append(int(input(f'Digite o {v}º número: ')))

num.sort(reverse=True)

print(num)