# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.,
from  time import sleep
def maior(*num):
    contador = maior = 0
    print('='*40)
    print('Analisando os valores recebidos...')
    for valor in num:
       print(f'{valor}  ', end='', flush=True)
       sleep(0.3)
       if contador == 0:
           maior = valor
       else:
           if valor > maior:
            maior = valor
       contador += 1
    print(f'Foram informados {contador} valores.')
    print(f'O maior valor informado foi {maior}')
#Programa Principal
maior(15,2,7,4,3,1,0,12)    
maior(2,6,4,12,8,5)
maior(22,56,32)
maior(12,5)
maior(8)
maior()