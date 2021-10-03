'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

print(20*'\033[1;31m=\033[m')
print('\033[1;40mNÚMERO PRIMO\033[m')
print('{}'.format(20*'\033[1;31m=\033[m'))


NumeroPrimo = int(input('Digite um numero inteiro: '))
tot = 0

for c in range(1,NumeroPrimo+1):
    if NumeroPrimo % c == 0:
        print('\033[32m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c),end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(NumeroPrimo,tot))

if tot == 2:
    print('E por isso ele é Primo!!')
else:
    print('E por isso ele Não é Primo')