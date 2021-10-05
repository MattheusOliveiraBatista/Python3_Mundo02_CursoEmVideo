'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
'''
# Minha solução
'''
numero = 0
soma = 0
qtd = 0

while not numero == 999:
   numero = int(input('Digite um numero [999 para parar]: '))

   if numero != 999:
       soma += numero
       qtd += 1

print('Você digitou {} números  e a soma entre eles foi {}.'.format(qtd,soma))
'''

#Solução dele

num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))

print('Você digitou \033[1;32m{}\033[m números e a soma entre eles foi \033[1;32m{}\033[m.'.format(cont,soma))