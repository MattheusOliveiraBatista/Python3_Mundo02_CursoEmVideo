'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print(25* '\033[1;34m=\033[m')
print('\033[1;40mSequência de Fibonacci\033[m')
print(25* '\033[1;34m=\033[m')

n = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
cont = 2
print('{} \033[1;34m->\033[m '.format(a), end='')

while cont <= n:
    fibo = a + b
    print('{} \033[1;34m-> \033[m'.format(fibo),end = '')
    b = a
    a = fibo 
    n -= 1
print('Fim da Sequência de Fibonacci')

