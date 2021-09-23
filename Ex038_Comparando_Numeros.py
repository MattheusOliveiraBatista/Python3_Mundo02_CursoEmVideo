'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('\nn1 = \033[1;31m{}\033[m e n2 = \033[1;31m{}\033[m '.format(n1, n2))

if n1 > n2:
    print('\nO \033[1;32mPrimeiro\033[m valor é maior que o \033[1;31mSegundo\033[m!')

elif n1 < n2:
    print('\nO \033[1;31mSegundo\033[m valor é maior que o \033[1;32mPrimeiro\033[m!')

else:
    print('\n\033[1;33mOs valores são iguais!\033[m') 