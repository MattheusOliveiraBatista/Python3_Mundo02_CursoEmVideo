'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

Nascimento = int(input('Ano de nascimento: '))

#date.today().year - Significa pegar o ano da data de hoje
idade =  date.today().year- Nascimento 

print('''Quem nasceu em \033[1;32m{}\033[m tem \033[1;32m{}\033[m anos em ''',end=''
'' '\033[1;32m{}\033[m '''.format(Nascimento, idade, date.today().year))

print(end=('\n'))

if(idade == 18):
    print('Você tem que se alistar \033[1;31mIMEDIATAMENTE\033[m')

elif(idade < 18):
    saldo = 18 - idade
    print('Você tem {} anos e falta {} anos para seu \033[1;33mALISTAMENTO\033[m!'.format(idade,saldo))
    ano = saldo + date.today().year
    print('Seu alistamento será em {}'.format(ano))

elif (idade > 18):
    print('Você já passou do \033[1;32mPrazo\033[m!')
    saldo = idade - 18
    ano = date.today().year - saldo
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))