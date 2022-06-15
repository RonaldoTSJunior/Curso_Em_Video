nome=str(input('Qual seu nome? ')).capitalize()
if nome=='Ronaldo':
    print('Que nome bonito!')
elif nome=='Patrick' or nome=='Claudio' or nome=='Cassiano':
    print('Que lindo o viadim mamando')
elif nome in 'Joao Antonio Jeferson Guilherme':
    print('Que bosta')
else:
    print('Seu nome é bem normal! ')
print(f'Entendido! Tenha um ótimo dia {nome}.')