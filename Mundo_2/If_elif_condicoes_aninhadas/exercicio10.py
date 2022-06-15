# Crie um programa de pedra papel tesoura
import random
novamente='s'
while novamente=='s':
    print('''---------REGRAS DO PEDRA PAPEL TESOURA!---------
[1] PEDRA!
[2] PAPEL!
[3] TESOURA!
''')
    computador=random.randint(1,3)
    jogador=int(input('Faça sua jogada!  '))
    if computador==1:
        print('Computador escolheu PEDRA! ')
        if jogador==1:
            print('EMPATE! ')
        elif jogador==2:
            print('Jogador ganhou! ')
        else:
            print('Computador ganhou! ')
    if computador==2:
        print('Computador escolheu PAPEL! ')
        if jogador==1:
            print('Computador ganhou! ')
        elif jogador==2:
            print('EMPATE! ')
        else:
            print('Jogador ganhou! ')
    if computador==3:
        print('Computador escolheu TESOURA! ')
        if jogador==1:
            print('Jogador ganhou! ')
        elif jogador==2:
            print('Computador ganhou! ')
        else:
            print('EMPATE! ')
    novamente=str(input('DESEJA JOGAR NOVAMENTE?\nS/N  ')).lower()