r1=float(input('Digite o comprimento da primeira reta: '))
r2=float(input('Digite o comprimento da segunda reta: '))
r3=float(input('Digite o comprimento da terceira reta: '))
if r1+r2>r3 and r1+r3>r2 and r3+r2>r1:
    print('Utilizando estas medidas, é possível criar um triângulo.')
else:
    r1+r2<=r3 and r1+r3<=r2 and r3+r2<=r1,print('Utilizando estas medidas é impossivel criar um triângulo.')
