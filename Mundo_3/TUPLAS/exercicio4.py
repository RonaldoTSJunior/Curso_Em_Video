# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
from lib2to3.pytree import convert


conversor=[]
numbers=()
contador_pares=0
for repeticao in range (4):
    user=int(input('Digite um número: '))
    conversor+=[user]
    numbers=tuple(conversor)
    if user % 2 == 0:
        contador_pares+=1
print("O primeiro número 3 se encontra na posição:",numbers.index(3))
print("O número 9 apareceu:",numbers.count(9),"vezes!")
print("A quantia de números pares na Tupla é:",contador_pares)
