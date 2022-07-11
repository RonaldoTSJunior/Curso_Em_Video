# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
aleatorios=()
lista_aleatorios=[]
for numeros in range(0,5):
    randoms=randint(0,101)
    lista_aleatorios.append(randoms)
    aleatorios=tuple(lista_aleatorios)
print("Os números sorteados na sua Tupla foram: ",aleatorios)
print("O maior valor presente nesta Tupla é: ",max(aleatorios))
print("O menor valor presente nesta Tupla é: ",min(aleatorios))