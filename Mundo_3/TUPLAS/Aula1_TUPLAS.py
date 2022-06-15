#Tuplas são imutáveis! Depois de criada, não pode ser alterada.
lanche=('Hamburguer','Suco','Pizza','Pudim','Batata Frita')
#lanche[2]='Maconha' Exemplo de que a tupla não pode ser alterada
# for contador in range(0,len(lanche)):
#     print(contador)
# for contador in range(0,len(lanche)):
#     print(lanche[contador])
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')
for posicao,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
    
#del() apaga a tupla inteira.
#variavel.index(tupla) mostra a posição em que o elemento dentro da tupla se encontra.