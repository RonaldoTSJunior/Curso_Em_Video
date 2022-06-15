#  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
print('''
      ---------JOGO DE ADVINHA---------
                 [INSTRUÇÕES]
    * Digite números de 1 a 10 até acertar *
    ''')
p1=999
contador=0
computador=random.randint(0,10)
print('''Já escolhi meu número.\nAgora é sua vez de advinhar!\nBoa Sorte!''')
sleep(1)
while p1!=computador:
    p1=int(input('Digite um número: '))
    if p1 == computador:
        contador+=1
        print(f'Você acertou!')
        print(f'Foram necessárias {contador} tentativas!')
    elif p1 > computador:
        contador+=1
        print('Menos...')
    elif p1 < computador:
        contador+=1
        print('Mais...')
sleep(1)
print('Finalizando...')