'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
num = 0 

while True:
    num = int(input('Digite o número que deseja calcular a tabuada: '))    
	
    if num < 0:
        break		
    
    for i in range(0,11):
        print(f'{num} x {i} = {num * i}')
	
