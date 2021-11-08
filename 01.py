"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
num = []

for v in range(1, 6):
    num.append(int(input(f"Digite o {v}º número: ")))

print(num)