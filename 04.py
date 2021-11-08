"""
Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

consoantes = []

for i in range(1, 11):
    letras = input(f"Digite a {i}ª letra: ").lower()

    if letras not in 'aeiou':
        consoantes.append(letras)

print(f'Foram digitadas {len(consoantes)} consoantes!')
print(f'Consoantes digitadas: {consoantes}')
