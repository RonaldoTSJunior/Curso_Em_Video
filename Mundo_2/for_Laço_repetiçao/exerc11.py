# desenvolva um programa que leia 'nome, idade, e sexo' de 4 pessoas. No final do programa, mostre: 
# a media de idade do grupo
# nome do homem mais velho
# quantas mulheres possuem menos de 20 anos
from time import sleep
print('''
    ---------[INSTRUÇÕES]---------
    .
    .
    .
    Genêros: M - Masculino, F - Feminino
    ''')
sleep(1)
contador_mulher=0
soma=0
media=0
maior=0
nome_velho=''
for analisador in range(4):
    nome=str(input('Digite seu primeiro nome: ')).capitalize().strip()
    sexo=str(input('Digite seu genêro: [M/F]  ')).upper()
    idade=int(input('Digite sua idade: '))
    soma+=idade
    media=soma/4
    if sexo=='M' and idade > maior:
        maior=idade
        nome_velho=nome
    elif sexo=='F' and idade < 20:
        contador_mulher+=1
print(f'''
O nome do homem mais velho é \033[31m{nome_velho}\033[m
Neste grupo tem \033[35m{contador_mulher}\033[m mulheres com menos de 20 anos
A media de idade deste grupo é \033[32m{media}\033[m
''')