#Faça um programa que leia um número entre '0' e '9999' e mostre na tela cada um dos digitos separados
#Ex: 1834
#Unidades: 4
#Dezenas: 3
#Centenas: 8
#Milhar: 1

n=int(input('Informe um número: '))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print(f'Analisando o número {n}')
print(f'O número tem {u} unidades')
print(f'O número tem {d} dezenas')
print(f'O número tem {c} centenas')
print(f'O número tem {m} milhar')