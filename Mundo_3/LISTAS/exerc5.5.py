#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
#for i in range(int(input('Quantos jogos deseja fazer? '))):
    #print(random.sample(range(1,60),6))
lista=[]
principal=[]
total=1
print('-='*50)
print(' '*30,'MEGA SENA')
print('-='*50)
user=int(input('Quantos jogos deseja fazer? '))
while total <= user:
    contador=0
    while True:
        numero=randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador+=1
        if contador >=6:
            break
    lista.sort()
    principal.append(lista[:])
    lista.clear()
    total+=1
for numerado,lista in enumerate(principal):
    print(f'Jogo N°{numerado} - {lista}')
fechar=str(input('Pressione ENTER para fechar.'))