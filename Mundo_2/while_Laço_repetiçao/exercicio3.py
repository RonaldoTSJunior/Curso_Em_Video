# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# # Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
print('''
      ---------MENU DE OPÇÕES---------
   * [ 1 ] somar
   * [ 2 ] multiplicar
   * [ 3 ] maior
   * [ 4 ] novos números
   * [ 5 ] sair do programa
                          [INSTRUÇÕES]
* Digite dois números inteiros e selecione uma das opções a cima! *       
      ''')
sleep(1)
opcoes=0
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
while opcoes!=5:
    opcoes=int(input('Escolha uma opção: '))
    if opcoes == 1:
        soma=n1+n2
        print(f'A sua escolha foi * [SOMAR] *.\n.\n.\n.\nO resultador de sua soma é {soma}')
    elif opcoes == 2:
        multiplicar=n1*n2
        print(f'A sua escolha foi * [MULTIPLICAR] *.\n.\n.\n.\nO resultado de sua multiplicação é {multiplicar}')
    elif opcoes == 3:
        if n1 > n2:
            print(f'A sua escolha foi * [MAIOR] *.\n.\n.\n.\nO maior número é {n1}')
        elif n1 < n2:
            print(f'A sua escolha foi * [MAIOR] *.\n.\n.\n.\nO maior número é {n2}')
        elif n1==n2:
            print(f'A sua escolha foi * [MAIOR] *.\n.\n.\n.\nOs seus dois números são iguais!')
    elif opcoes == 4:
        print('A sua escolha foi * [NOVOS NÚMEROS] *.')
        n1=int(input('Digite um número: '))
        n2=int(input('Digite outro número: '))
    elif opcoes == 5:
        print('A sua escolha foi [SAIR DO PROGRAMA].\nFinalizando...')
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
    sleep(1)
print('Adeus!!!')