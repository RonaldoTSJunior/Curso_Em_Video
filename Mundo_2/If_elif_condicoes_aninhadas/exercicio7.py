# Refaça o exericio 8 da pasta "condições", acrescentando o tipo de triangulo que será formado
# equilátero - todos os lados iguais 
# isósceles - dois lados iguais 
# escaleno - todos os lados diferentes
escolha='s'
while escolha=='s':  
    r1=float(input('Digite o comprimento da primeira reta: '))
    r2=float(input('Digite o comprimento da segunda reta: '))
    r3=float(input('Digite o comprimento da terceira reta: '))
    if r1+r2>r3 and r1==r2==r3:
        print('Utilizando estas medidas, é possível criar um triângulo.\nSeu triângulo é um EQUILÁTERO.') 
    elif r1+r3>r2 and r1==r2!=r3:
        print('Utilizando estas medidas, é possível criar um triângulo.\nSeu triângulo é um ISÓSCELES.')
    elif r3+r2>r1 and r1!=r2!=r3:
        print('Utilizando estas medidas, é possível criar um triângulo.\nSeu triângulo é um ESCALENO.')
    else:
        r1+r2<=r3 and r1+r3<=r2 and r3+r2<=r1,print('Utilizando estas medidas é impossivel criar um triângulo.')
    escolha=str(input('DESEJA REPETIR A OPERAÇÃO?\n[S/N] ')).lower()
