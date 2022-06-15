# Crie um programa que leia um numero inteiro e diga se ele é um numero primo
n=int(input('Digite um número: '))
tot=0
for c in range(1,n+1):
    if n % c==0:
        print('\033[33m',end=' ')
        tot+=1
    else:
        print('\033[31m',end=' ')
    print(f'{c}\033[m', end=' → ')
print(f'\nSeu número {n} foi divisível {tot} vezes. ')
if tot==2:
    print('Seu número é primo! ')
else:
    print('Seu número não é primo! ')