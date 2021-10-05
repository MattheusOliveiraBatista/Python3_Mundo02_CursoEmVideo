'''
Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. 
É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

#EXEMPLO DO COMANDO Break


while True:
    if terra:
        passo
    
    if vazio:
        pula
    
    if moeda:
        pega

    if trofeu:
        pula 
        break
pega
'''
'''
cont = 1

#while cont <= 10:
while True:
    print(cont, ' ->  ', end='')
    cont += 1
print('Acabou')
'''

num  = s = 0

while True:
    num = int(input('Digite um número: '))
    if num== 999:
        break
    s += num
print(f'A soma vale {s}') #PYTHON 3.6+
#print('A soma vale {}'.format(s)) #PYTHON 3
#print('A soma  vale %d',%(s)) #PYTHON 2