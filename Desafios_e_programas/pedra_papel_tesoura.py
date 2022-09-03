'''
PEDRA GANHA DE TESOURA
PAPEL GANHA DE PEDRA
TESOURA GANHA DE PAPEL
'''
import random
from time import sleep
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
        sleep(1)
        print('Computador escolheu PEDRA ')
        sleep(1)
        if p1==1:
            print('EMPATE!')
            sleep(1)
        elif p1==2:
            print('Player ganhou!')
            sleep(1)
        elif p1==3:
            print('Computador ganhou! ')
            sleep(1)
    elif computador==2:
        sleep(1)
        print('Computador escolheu PAPEL ')
        sleep(1)
        if p1==1:
            print('Computador ganhou! ')
            sleep(1)
        elif p1==2:
            print('EMPATE! ')
            sleep(1)
        elif p1==3:
            print('Player ganhou! ')
            sleep(1)
    elif computador==3:
        sleep(1)
        print('Computador escolheu TESOURA ')
        sleep(1)
        if p1==1:
            print('Player ganhou! ')
            sleep(1)
        elif p1==2:
            print('Computador ganhou! ')
            sleep(1)
        elif p1==3:
            print('EMPATE! ')
            sleep(1)
    jogar_novamente=str(input('Deseja jogar novamente? s/n   ')).lower()