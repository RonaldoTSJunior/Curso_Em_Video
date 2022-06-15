from cmath import sqrt
import math
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente: '))
print(f'O comprimento do cateto oposto é: {co}, o comprimento do cateto adjacente é: {ca}, e valor da raiz hipotenusa é: {math.hypot(co,ca):.2f}')