'''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
'''
pesoMenor = 0
pesoMaior = 0

for peso in range(1,6):
    pesoPessoa = float(input('Digite o pessoa da {}°: '.format(peso)))

    if peso == 1:
        pesoMenor = pesoPessoa
        pesoMaior = pesoPessoa

    else:
        if pesoPessoa > pesoMaior:
            pesoMaior = pesoPessoa
        if pesoPessoa < pesoMenor:
            pesoMenor = pesoPessoa

print('O Maior Peso lido foi de {} Kg'.format(pesoMaior))
print('O Menor Peso lido foi de {} Kg'.format(pesoMenor))