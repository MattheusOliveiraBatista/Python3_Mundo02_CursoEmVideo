'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'sS':
    numeros = int(input('Digite um valor: '))
    soma += numeros
    quant +=1    
    if quant == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma/quant
print('\nVocê digitou {} números e a média foi {:.2f}'.format(quant,media))
print('\nO maior valor foi {} e o menor foi {}'.format(maior, menor))
