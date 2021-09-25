'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''

PrimeiraNota = float (input('Digite a primeira nota: '))
SegundaNota = float (input('Digite a segunda nota: '))

media = (PrimeiraNota + SegundaNota)/2

if media >= 7:
    print('Parabéns, você está \033[1;32mAprovado! :)\033[m')

elif media >= 5 and media < 6.9:
    print('Você está de \033[1;33mRecuperação!\033[m')

elif media < 5:
    print('VocÊ está \033[1;31mReprovado! \033[m :(')