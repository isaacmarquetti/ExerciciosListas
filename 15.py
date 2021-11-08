"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""

notas = []

v = cont = soma = media = maior = menor = 0

while True:
    cont += 1
    v = float(input(f"Digite o {cont}º número: "))
    notas.append(v)
    if v == -1:
        notas.pop(-1)
        break

print(f'Quantidade de valores lidos: {cont-1}')
print(f'Notas: {notas}')
notas.reverse()
for nota in notas:
    print(nota)
    soma += nota

print(f'Soma das notas: {soma}')
media = soma / (cont - 1)
print(f'Média das notas: {media:.1f}')

for nota in notas:
    if nota >= media:
        maior += 1
    if nota < 7:
        menor += 1

print(f'Acima da média calculada: {maior} notas')
print(f'Abaixo de 7: {menor} notas')
print(f'Obrigado! Volte sempre!')
