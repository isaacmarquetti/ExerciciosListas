"""
Faça um Programa que leia 20 números inteiros e
armazene-os num vetor. Armazene os números pares no vetor PAR
e os números IMPARES no vetor impar. Imprima os três vetores.
"""
numeros = []
par = []
impar = []
num = 0

for v in range(1, 21):
    num = int(input(f"Informe o {v}º número: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Vetor dos números: {numeros}')
print(f'Vetor dos pares: {par} ')
print(f'Vetor dos ímpares: {impar}')


