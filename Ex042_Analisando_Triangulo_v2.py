'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''
print('\033[1;32m-=-\033[m'*10)
print('Analisador de Triângulos')
print('\033[1;32m-=-\033[m'*10)
print('\n')

PrimeiroValor = int(input('Digite o Primeiro Valor: '))
SegundoValor = int(input('Digite o Segundo Valor: '))
TerceiroValor = int(input('Digite o Terceiro Valor: '))

if PrimeiroValor < SegundoValor + TerceiroValor and SegundoValor < PrimeiroValor + TerceiroValor and TerceiroValor < SegundoValor + PrimeiroValor:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if(PrimeiroValor == SegundoValor and SegundoValor == TerceiroValor):
        print('Triângulo \033[1;32mEQUILÁTERO!\033[m')

    elif(PrimeiroValor != SegundoValor and SegundoValor != TerceiroValor):
        print('Triângulo \033[1;34mESCALENO!\033[m')
    else: 
        print('Triângulo \033[1;33mISÓSCELES!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')