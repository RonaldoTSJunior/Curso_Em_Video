#Crie um programa que leia o nome de uma pessoa e diga se possui a palavra 'SILVA' em qualquer parte do nome dela,

n=str(input('Digite o seu nome: ')).lower().split()
print('Analisando o seu nome...')
print(f'O seu nome possui silva na composição? {"silva" in n}')