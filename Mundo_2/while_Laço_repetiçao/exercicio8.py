#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n=0
contador=0
soma=0
while n != 999:
    n=int(input('Digite um número: '))
    contador+=1
    soma+=n
    print(f'O número digitado foi: {n}')
    if n == 999:
        print(f'Sequência terminada, a quantia de número digitados foi {contador}.\nE a soma entre eles é {soma-999}.')
print('Programa Finalizado.')