# Faça um programa que leia o peso de 5 pessoas, e no final diga qual é o maior e o menor peso.
from time import sleep
print('''
---------BALANÇA---------
''')
sleep(1)
lista=[]
for balanca in range(5):
    nome=str(input('Digite seu primeiro nome: ')).capitalize()
    peso=float(input('Digite seu peso atual: '))
    lista+=[peso]
print(f'O maior peso é',max(lista))
print(f'O menor peso é',min(lista))