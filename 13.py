"""
Faça um programa que receba a temperatura média de cada mês do ano
e armazene-as em uma lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso:
1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = ('1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho', '8 - Agosto',
         '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro')

temperaturas = {}

soma = media = 0

print("Digite a temperatura média dos meses do ano")

for mes in meses:
    temperaturas[mes] = float(input(f' {mes} : '))

for temp in temperaturas.values():
    soma += temp

media = soma / 12

print(f"Acima da média anual: {media:.2f}")

for mes in meses:
    if temperaturas[mes] >= media:
        print(f'{mes}: {temperaturas[mes]}')

