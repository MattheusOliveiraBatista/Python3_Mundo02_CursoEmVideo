'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
num1  = int(input('Primeiro valor: '))
num2  = int(input('Segundo valor: '))

opcao = 0

#if opcao != range(0,6):
while opcao != 5:

    print(15 * '\033[1;32m*\033[m')
    print('''\033[1;40m 
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do Programa
    \033[m''') 
    print(15 * '\033[1;32m*\033[m')


    opcao = int (input('Qual é a sua opção? '))
    if opcao == 1:
        print('\n\033[1;31mOpção de Somar escolhida!\033[m')
        print('{} + {} = {}'.format(num1, num2, num1+num2))
    
    if opcao == 2:
        print('\n\033[1;32mOpção de Multiplicar escolhida!\033[m')
        print('{} * {} = {}'.format(num1, num2, num1*num2))
    
    elif opcao == 3:
        print('\n\033[1;33mOpção de Maior e Menor escolhida!\033[m')
        if num1 > num2:
            print('\nMaior valor foi: {}'.format(num1))
            print('Menor valor foi: {}'.format(num2))
        else:
            print('\nMaior valor foi: {}'.format(num2))
            print('Menor valor foi: {}'.format(num1))
    
    elif opcao == 4:
        print('\n\033[1;34mOpção de Mudar valores escolhida!\033[m')
        num1  = int(input('Primeiro valor: '))
        num2  = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Programa Finalizado!\nVolte sempre! :)')
    
    else:
        print('Opção Inválida, tente novamente!')
    sleep(2)