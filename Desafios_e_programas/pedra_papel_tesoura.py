'''
PEDRA GANHA DE TESOURA
PAPEL GANHA DE PEDRA
TESOURA GANHA DE PAPEL
'''
import random
jogar_novamente='s'
while jogar_novamente=='s':
    print('''------BEM VINDO AO PEDRA PAPEL OU TESOURA!------
[1] PEDRA
[2] PAPEL 
[3] TESOURA
''')
    computador=random.randint(1,3)
    p1=int(input('Digite sua escolha: '))
    if computador==1:
        print('Computador escolheu PEDRA ')
        if p1==1:
            print('EMPATE!')
        elif p1==2:
            print('Player ganhou!')
        elif p1==3:
            print('Computador ganhou! ')
    elif computador==2:
        print('Computador escolheu PAPEL ')
        if p1==1:
            print('Computador ganhou! ')
        elif p1==2:
            print('EMPATE! ')
        elif p1==3:
            print('Player ganhou! ')
    elif computador==3:
        print('Computador escolheu TESOURA ')
        if p1==1:
            print('Player ganhou! ')
        elif p1==2:
            print('Computador ganhou! ')
        elif p1==3:
            print('EMPATE! ')
    jogar_novamente=str(input('Deseja jogar novamente? s/n   ')).lower()