nome = str(input('Qual é o seu nome? ')).strip()

if nome == 'Matheus':
    print('Que nome perfeito!! :)')

elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')

elif nome in 'Ana Cláudia Jéssica Paula':
    print('Ótimo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
