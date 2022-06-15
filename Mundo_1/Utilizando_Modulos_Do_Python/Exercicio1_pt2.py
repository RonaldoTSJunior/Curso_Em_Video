#Crie um programa que leia o nome completo de uma pessoa mostre:
#O nome completo com todas as letras maiusculas
#O nome completo com todas as letras minusculas
#Quantas letras ao todo sem contar os espaços
#Quantas letras tem o primeiro nome




nome=str(input('Digite o nome completo: ')).strip()
print('Analisando seu nome... ')
print(f'O nome completo é:{nome}')
print(f'O nome em maisculuas é : {nome.upper()}')
print(f'O nome em minusculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'O seu primeiro nome tem {nome.find(" ")} letras')