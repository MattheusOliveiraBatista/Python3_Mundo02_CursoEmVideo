'''''''''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)
'''

n = int(input('Digite um numero para o For: '))

for c in range(0,n,1):
    print('Índice [{}]'.format(c))

print('\nFimmm :)')