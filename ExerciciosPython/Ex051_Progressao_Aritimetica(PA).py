'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print(20*'\033[1;32m=\033[m')
print('\033[1;31m10 TERMOS DE UMA PA\033[m')
print('{}'.format(20*'\033[1;32m=\033[m'))


PrimeiroTermo = int(input('Digite o Primeiro Termo da PA: '))
Razao = int(input('Digite a Razão da PA: '))
decimo = PrimeiroTermo + (10-1) * Razao

for c in range(PrimeiroTermo,decimo+Razao,Razao):
    print('{}'.format(c), end = ' -> ')
print('Fim! :)')