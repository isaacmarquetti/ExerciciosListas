"""
Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

pessoa = []

for i in range(1, 6):
    dados = []
    print(f"Pessoa {i}:")
    dados.append(int(input("Idade: ")))
    dados.append(float(input("Altura(m): ")))
    pessoa.append(dados)

pessoa.reverse()

for dados in pessoa:
    print('-------------------')
    print(f'Idade: {dados[0]}')
    print(f'Altura: {dados[1]}')

