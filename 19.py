"""
Uma empresa de pesquisas precisa tabular os resultados da
seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado
da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0,
que encerra a entrada dos dados. Não deverão ser aceitos valores
além dos válidos para o programa (0 a 6). Os valores referentes a
cada uma das opções devem ser armazenados num vetor. Após os dados
terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da
enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40% dos votos.
"""

sistema = {'Windows Server': 0, 'Unix': 0, 'Linux': 0, 'Netware': 0, 'Mac OS': 0, 'Outro': 0}

total_votos = 0

while True:
    voto = int(input("Digite o voto: "))

    if voto == 0:
        break
    elif voto == 1:
        sistema['Windows Server'] += 1
        total_votos += 1
    elif voto == 2:
        sistema['Unix'] += 1
        total_votos += 1
    elif voto == 3:
        sistema['Linux'] += 1
        total_votos += 1
    elif voto == 4:
        sistema['Netware'] += 1
        total_votos += 1
    elif voto == 5:
        sistema['Mac OS'] += 1
        total_votos += 1
    elif voto == 6:
        sistema['Outro'] += 1
        total_votos += 1
    else:
        print("Informe um valor entre 1 e 6 (0 para sair)")


print(sistema)
print(f'Total de votos: {total_votos}')

porc = 0

print('Sistema Operacional   Votos   %')
print('-------------------   -----   ---')

for v, i in sistema.items():
    porc = i / total_votos * 100
    print(f'{v:21s} {i:5d}   {porc:.0f}%')

