# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista_numeros=[]
for numeros in range(5):
    lista_numeros.append(int(input('Digite um valor: ')))
    maior=max(lista_numeros)
    menor=min(lista_numeros)
posicao1=lista_numeros.index(maior)
posicao2=lista_numeros.index(menor)
print(f'O maior número de sua lista é: {maior}.\n E se encontra na posição {posicao1}')
print(f'O menor número de sua lista é: {menor}.\n E se encontra na posição {posicao2}')