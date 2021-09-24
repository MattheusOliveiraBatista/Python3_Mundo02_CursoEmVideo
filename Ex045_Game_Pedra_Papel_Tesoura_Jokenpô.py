'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
itens = ('Pedra', 'Papel', 'Tesoura')

from random import randint
from time import sleep

computador = randint(0,2)

print('''Suas opções: 
\033[1;34m
[0] - Pedra
[1] - Papel
[2] - Tesoura
\033[m''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('\033[1;31m-=-\033[m'*10)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('\033[1;31m-=-\033[m'*10)

if( computador == 0):
    
    if(jogador == 0):
        print('\033[1;33mEMPATE!\033[m')

    elif(jogador == 1):
        print('\033[1;32mJOGADOR VENCEU!\033[m')

    elif(jogador == 2):
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')

    else:
        print('Opção Inválida!!')

elif( computador == 1):
    if(jogador == 1):
        print('\033[1;33mEMPATE!\033[m')

    elif(jogador == 2):
        print('\033[1;32mJOGADOR VENCEU!\033[m')

    elif(jogador == 0):
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')

    else:
        print('Opção Inválida!!')

elif( computador == 2):
    if(jogador == 2):
        print('\033[1;33mEMPATE!\033[m')

    elif(jogador == 0):
        print('\033[1;32mJOGADOR VENCEU!\033[m')

    elif(jogador == 1):
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')

    else:
        print('Opção Inválida!!')