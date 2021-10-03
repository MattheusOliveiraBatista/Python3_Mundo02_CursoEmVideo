'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.
'''

somaIdade = 0
NomeVelho = ''
idadeMaior = 0
qtdMulher = 0

for dados in range(1,5):
    print('----- {}° PESSOA ----'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int (input('Idade: '))
    sexo =  str(input('Sexo [M/F]: ')).strip()

    if sexo == "M" or sexo == "m":
        if idade > idadeMaior:
            idadeMaior = idade
            NomeVelho = nome

    if sexo == "f" or sexo == "F":
        if idade  < 20:
            qtdMulher += 1
    
    
    somaIdade += idade

print('A média de idade do grupo é de {} anos '.format(somaIdade/4))
print('O home mais velho tem {} anos e se chama {}'.format(idadeMaior,NomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(qtdMulher))

'''
somaidade = 0
mediaidade = 0 
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for dados in range(1,5):
    print('----- {}° PESSOA ----'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int (input('Idade: '))
    sexo =  str(input('Sexo [M/F]: ')).strip()
    somaidade += idade 

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade/4
print('A média de idade do grupo é de {} anos '.format(mediaidade))
print('O home mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''