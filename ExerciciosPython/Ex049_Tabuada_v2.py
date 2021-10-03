'''
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

numero = int(input('Digite um número para ver sua tabuada: '))

print('\n')
print(15 * '\033[1;32m*\033[m')
print('TABUADA DO N°: {}\n'.format(numero))
for c in range(0,11):
    if (numero*c < 10):
        print('{} x {} = 0{}'.format(numero, c,numero*c))
    else:
        print('{} x 0{} = {}'.format(numero, c,numero*c))


print(15 * '\033[1;32m*\033[m')