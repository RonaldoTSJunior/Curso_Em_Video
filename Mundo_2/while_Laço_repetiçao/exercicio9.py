# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contador=0
escolha='s'
n=0
soma=0
media=0
maior=[]
while escolha=='s':
    while escolha!='n':
        n=int(input('Digite um número: '))
        escolha=str(input('Deseja continuar a digitar valores? [S/N]: ')).lower().strip()
        contador+=1
        soma+=n
        maior+=[n]
    media=soma/contador
    print("O maior valor é:",max(maior),"\nO menor valor é:",min(maior))
    print(f'A média dos valores digitados é {media:.2f}\nE a quantia de números digitados foi {contador}')
print('Finalizando...')