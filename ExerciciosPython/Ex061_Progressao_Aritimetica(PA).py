'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.
'''

PTermo = int(input('Digite o valor do primeiro termo: '))
Razao = int(input('Digite o valor da razão: '))
termo = PTermo
contador = 1

while contador <= 10:
    print('\033[1;40m{}\033[m \033[1;31m-> \033[m'.format(termo), end = '')
    termo += Razao
    contador +=1
print('Fim :)')