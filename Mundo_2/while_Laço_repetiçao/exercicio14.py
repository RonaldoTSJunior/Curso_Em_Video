#  Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
total_produtos=0
total_compra=0
total_1000=0
preco_menor=0
nome_barato=''
while True:
    print('-='*25)
    nome=str(input('Digite o nome do produto: ')).capitalize().strip()
    print('-='*25)
    preco=float(input('Digite o preço de seu produto: R$ '))
    print('-='*25)
    total_produtos+=1
    escolha=str(input('Deseja Continuar? [S/N]: ')).upper().strip()
    total_compra+=preco
    if preco>1000:
        total_1000+=1
    if total_produtos==1:
        preco_menor=preco
        nome_barato=nome
    else:
        if preco < preco_menor:
            preco_menor=preco
            nome_barato=nome
    if escolha=='N':
        print(f'O total de suas compra é R${total_compra}.\n{total_1000} produtos custam mais que R$1000,00.\nE o nome do produto mais barato é {nome_barato}.')
        print('-='*25)
        print('Finalizando...')
        break
        