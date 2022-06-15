# : Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
from time import sleep
soma=contador=0
print('PAR OU ÍMPAR!')
print('-='*25)
while True:
    nome=str(input('Digite seu nome! ')).capitalize().strip()
    print('.\n.\n.')
    sleep(1)
    print(f'Já fiz minha jogada! Agora é sua vez {nome}.')
    jogador=int(input('Digite um número: '))
    escolha=str(input('P ou I? ')).upper().strip()
    print('-='*25)
    computador=randint(0,10)
    soma=computador+jogador
    if soma % 2 == 0:
        if escolha == 'P':
            contador+=1
            print(f'{nome} escolheu PAR e o número {jogador}, o computador escolheu {computador}. Total de {soma}, {nome} Ganhou!!')
        elif escolha == 'I':
            print(f'{nome} escolheu ÍMPAR e o número {jogador}, o computador escolheu {computador}. Total de {soma}, Computador Ganhou!!')
            print(f'Finalizando...\nO total de vitórias consecutivas é {contador}')
            break
    elif soma % 2 != 0:
        if escolha == 'I':
            contador+=1
            print(f'{nome} escolheu ÍMPAR e o número {jogador}, o computador escolheu {computador}. Total de {soma}, {nome} Ganhou!!')
        elif escolha == 'P':
            print(f'{nome} escolheu PAR e o número {jogador}, o computador escolheu {computador}. Total de {soma}, Computador Ganhou!!')
            print(f'Finalizando...\nO total de vitórias consecutivas é {contador}')
            break
choice=str(input('aperte qualquer tecla para fechar '))