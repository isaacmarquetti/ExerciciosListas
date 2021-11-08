"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão
ser compostos pelos elementos intercalados dos dois outros vetores.

Altere o programa anterior, intercalando 3 vetores de
10 elementos cada.
"""

vetor_a = []
vetor_b = []
vetor_c = []
vetor_d = []

print('Informe os valores do primeiro vetor')
for v in range(1, 11):
    vetor_a.append(int(input(f' Digite o {v}º número: ')))

print('Informe os valores do segundo vetor')
for v in range(1, 11):
    vetor_b.append(int(input(f' Digite o {v}º número: ')))

print('Informe os valores do terceiro vetor')
for v in range(1, 11):
    vetor_c.append(int(input(f' Digite o {v}º número: ')))

# intercalando valores
for i in range(0, 10):
    vetor_d.append(vetor_a[i])
    vetor_d.append(vetor_b[i])
    vetor_d.append(vetor_c[i])

print(vetor_d)