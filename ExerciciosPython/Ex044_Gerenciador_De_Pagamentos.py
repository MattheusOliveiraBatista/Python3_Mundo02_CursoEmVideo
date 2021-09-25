'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
'''

print('\033[1;31m======\033[m LOJA DO MATHEUS \033[1;31m======\033[m')
preco = float(input('Preço das compras: R$ '))

print('\n\033[1;33mFORMAS DE PAGAMENTO\033[m')

print('''\033[1;34m
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão
\033[m''')

op = int(input('Qual é a opção? '))

if (op == 1):
    valor = preco - ((preco*10)/100)
    print('\nSua compra de R$:{:.2F} vai custar R$:{:.2F} no final.'.format(preco, valor))

elif (op == 2):
    valor = preco - ((preco*5)/100)
    print('\nSua compra de R$:{:.2F} vai custar R$:{:.2F} no final.'.format(preco, valor))

elif (op == 3):
    valor = preco / 2
    print('\nSua compra de R$:{:.2F} será parcelada em 2 x R$:{:.2F} sem juros.'.format(preco,valor))

elif (op == 4):
    valor =  preco + ((preco * 20)/100)
    parcela = int(input('Digite a quantidade de parcelas: '))    
    valorParcelado = valor/parcela
    
    print('\nSua compra será parcela em {} x R${} COM JUROS'.format(parcela,valorParcelado))
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,valor))

else:
    print('\n\033[1;31mOpção Inválida! :( \033[m')