'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year

totMaior = 0
totMenor = 0

for pess in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        totMaior += 1
        print('Essa pessoa é maior!')
    else:
        totMenor += 1
        print('Essa pessoa é de menor!')

print('A quantidade de Pessoas Maiores e Menores foram: {}, {}'.format(totMaior,totMenor))