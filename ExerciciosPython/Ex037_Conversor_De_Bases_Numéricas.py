'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será 
a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

numero = int(input('Digite um numero inteiro: '))

print('\n')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL\n')
opcao = int(input('Sua opção: '))


if( opcao == 1):
    print('\n{} convertido para BINÁRIO é igual  a {}'.format(numero,bin(numero)))
elif (opcao == 2):
    print('\n{} convertido para OCTAL é igual  a {}'.format(numero,oct(numero)))
elif (opcao == 3):
    print('\n{} convertido para HEXADECIMAL é igual  a {}'.format(numero,hex(numero)))

else:
    print('Opção inválida! Tente Novamente! :(')