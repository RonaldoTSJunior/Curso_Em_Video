# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import sample
aleatorios=tuple(sample(range(999),5))
print('Os números escolhidos foram:\n',aleatorios)
print(f'O maior número da tupla é:',max(aleatorios))
print(f'O menor número da tupla é:',min(aleatorios))