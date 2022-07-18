# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros=[]
escolha='s'
contador=0
while escolha=='s':
    user=int(input('Digite um valor: '))
    numeros.append(user)
    contador+=1
    escolha=str(input('Deseja continuar? [S/N]: ')).lower().strip()
if 5 in numeros:
    print('O número 5 está presente na lista! Se encontra na posição:',numeros.index(5))
else:
    print('O número 5 não está presente na lista!!')
if escolha == 'n':
    numeros.sort(reverse=True)
    print('Sua lista invertida ficou assim:\033[0;31;m',numeros,'\033[m')
    print('A quantia de números digitados foi de:',contador)
