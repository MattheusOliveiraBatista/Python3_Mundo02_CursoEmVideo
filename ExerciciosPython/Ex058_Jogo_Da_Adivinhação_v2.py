'''
 Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
 Só que agora o jogador vai tentar adivinhar até acertar, 
 mostrando no final quantos palpites foram necessários para vencer.
'''

import random

computador = random.randint(0,10)

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? \n')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;32mMais...Tente mais uma vez\033[m.')
        elif jogador > computador:
              print('\033[1;31mMenos...Tente mais uma vez\033[m.')
print('\033[1;40mAcertou com {} tentativas\033[m. \033[1;33mParabéns\033[m'.format(palpites))
