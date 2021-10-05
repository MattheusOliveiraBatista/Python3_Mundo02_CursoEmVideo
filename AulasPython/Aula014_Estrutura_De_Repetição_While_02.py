'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a 
estrutura de repetição while no Python. Por exemplo:

c=1 while c !=10:

print(c)

c+=1

print(‘Acabou’)
'''

'''
for c in range(1,10):
    print(c)
print('Fim')

'''
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''

'''
r = 'S'

while r == 'S' or r == 's':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N] ')).strip()

print('Fim :)')

'''

n = 1
par = 0 
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1

print('Você digitou {} números Pares e {} número Ímpares'.format(par, impar))