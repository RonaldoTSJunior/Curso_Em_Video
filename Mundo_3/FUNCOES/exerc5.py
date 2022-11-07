#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = list()
par = list()


def sorteia():
    for repetidor in range(5):
        sorteio = randint(0,10)
        if sorteio % 2 == 0:
            par.append(sorteio)
        numeros.append(sorteio)
    print(f'Seus números sorteados são: {numeros}')
    
    
def somaPar():
    soma = sum(par)
    print(f'A soma dos números pares sorteados de {numeros} é: {soma}')
    
    
#Programa Principal
sorteia()
somaPar()
