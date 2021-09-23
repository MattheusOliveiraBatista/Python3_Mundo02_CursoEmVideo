'''
A Confederação Nacional de Natação precisa de um programa que leia o 
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

from datetime import date 

nascimento = int(input('Em que ano você nasceu? '))

atual  = date.today().year
idade = atual - nascimento

print('O Atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Você está na categoria \033[1;30mMIRIM!\033[m')

elif idade > 9 and idade <= 14:
     print('Você está na categoria \033[1;31mINFANTIL!\033[m')

elif idade > 14 and idade <= 19:
    print('Você está na categoria \033[1;32mJÚNIOR!\033[m')

elif idade > 19 and idade <= 25:
    print('Você está na categoria \033[1;33mSÊNIOR!\033[m')

elif idade > 25:
    print('Você está na categoria \033[1;34mMASTER!\033[m')