# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
contador_maior_18=0
contador_menor_20=0
contador_homens=0
idade=0
sexo=''
nome=''
while True:
    print('-='*25)
    nome=str(input('Digite seu nome: ')).capitalize().strip()
    print('-='*25)
    sexo=str(input('Digite seu gênero [M/F]: ')).upper().strip()
    print('-='*25)
    idade=int(input('Digite sua idade: '))
    print('-='*25)
    escolha=str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print('-='*25)
    if idade>18:
        contador_maior_18+=1
    if idade<20 and sexo=='F':
        contador_menor_20+=1
    if sexo=='M':
        contador_homens+=1
    if escolha=='N':
        print('Tudo bem! Então vamos lá.')
        print('-='*25)
        print(f'O total de pessoas com mais de 18 anos é {contador_maior_18}\nO total de homens é {contador_homens}\nE neste grupo temos {contador_menor_20} mulheres com menos de 20 anos!')
        print('-='*25)
        print('Finalizando')
        print('-='*25)
        break
        
    
