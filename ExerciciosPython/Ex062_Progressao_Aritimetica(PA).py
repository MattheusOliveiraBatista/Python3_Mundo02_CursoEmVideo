'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''


       
       # print('\033[1;40m{}\033[m \033[1;31m-> \033[m'.format(termo), end = '')
 
print("="*20)
print("PROGRESSÃO DE UMA PA")
print("="*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contador = 0
total = 10
mais = 0
while contador < total:
    while contador < total:
        print('\033[1;40m{}\033[m \033[1;31m-> \033[m'.format(termo), end = '')
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer? "))
    if mais == 0:
        contador = total
    total += mais
print("\nProgressão finalizada com o total de {} termos".format(total))