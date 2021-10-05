'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
'''
# INÍCIO DO CÓDIGO USANDO BIBLIOTECA
from math import factorial

numero = int(input('\nDigite um número para calcular seu Fatorial: '))
fat = factorial(numero)

print('O fator de {} é {}.'.format(numero,fat))
#FIM DO CÓDIGO USANDO BIBLIOTECA

contador = numero
print('\n\033[1;32mCalculando {}!\033[m = ' .format(numero), end = '')
f = 1

#USANDO O FOR 
for c in range(contador,0, -1 ):
    print('\033[1;32m{}\033[m'.format(c), end='')
    print('\033[1;40m x \033[m'if c > 1 else '\033[1;40m = \033[m', end = '')
    f *= c
print('{}'.format(f))

#USANDO O WHILE
'''
while  contador > 0:
    print('\033[1;32m{}\033[m'.format(contador), end='')
    print('\033[1;40m x \033[m'if contador > 1 else '\033[1;40m = \033[m', end = '')
    f *= contador 
    contador -=1
print('{}'.format(f))

'''