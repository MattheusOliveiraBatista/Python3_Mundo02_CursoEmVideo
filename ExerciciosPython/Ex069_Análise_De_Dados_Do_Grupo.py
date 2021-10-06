'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

MaiorDeIdade = Homens = MulheresMenor = 0
resp = ''

while True:
    print(20*'-')
    print('CADASTRE UMA PESSOA')
    print(20*'-')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if idade> 18:
        MaiorDeIdade +=1
    if sexo == 'M':
        Homens += 1
    if sexo == 'F'and idade < 18:
        MulheresMenor += 1

    resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    
    if  resp  == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {MaiorDeIdade}')     
print(f'Ao todo temos {Homens} homens cadastrados.')
print(f'E temos {MulheresMenor} mulheres com menos de 20 anos.')