'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valorCasa = float(input('Qual seria o valor da casa que deseja comprar? R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input('Em quantos pretende pagar a casa? '))

print('\nSeu salário: {}'.format(salario))
print('Valor do Imóvel: {}'.format(valorCasa))
print('Tempo que a casa será paga: {}'.format(anos))

prestacao = valorCasa / (anos*12)
salarioPorcento = salario*30/100

print('\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(valorCasa,anos,prestacao))

if (salarioPorcento < prestacao):
    print('Empréstimo Negado! :(')

else:
    print('\nParabéns você acaba de comprar uma casa nova! :)')
    print('Empréstismo concedido!')