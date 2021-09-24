'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida

'''

peso = float(input('Qual é o seu peso (Kg)? '))
altura = float(input('Qual é a sua altura (m)? '))

imc = peso/(altura*altura)

print('Imc do usuário informado: {:.2f}'.format(imc))

if imc < 18.5:
    print('\033[1;31mAbaixo do Peso!\033[m')

elif imc >= 18.5 and imc < 25:
        print('\033[1;32mPeso Ideal!\033[m')
        
elif imc >= 25 and imc < 30:
        print('\033[1;33mSobrePeso!\033[m')

elif imc >= 30 and imc < 40:
    print('\033[1;31mObesidade!\033[m')

else:
    print('\033[1;31mObesidade Mórbida! :( :(\033[m')
    print('\033[1;31mS.O.S Médico já! :( :(\033[m')
