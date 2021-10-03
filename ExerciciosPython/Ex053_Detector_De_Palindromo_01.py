'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras  = frase.split()
#print("Você digitou a frase: {}".format(palavras))
junto  = ''.join(palavras)
#print("Você digitou a frase: {}".format(junto))
inverso = ''

                    #tamanho - 1, vai até o index -1 (0), decrementando
for letra in range(len(junto)- 1, -1, -1):
    inverso += junto[letra]
print('O inverso {} é {}'.format(junto,inverso))

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')