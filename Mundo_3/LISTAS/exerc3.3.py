# # Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# # No final, mostre a matriz na tela, com a formatação correta.


# matriz=[]
# posicoes=[]
# contador1=0
# contador2=0
# contador3=0
print('-='*60)
print(' '*30,'MATRIZ 3X3!')
print(' '*15,"FAVOR INSERIR APENAS NUMEROS INTEIROS!!")
print('-='*60)
# for sequencia in range(3):
#     posicoes.append(int(input(f'Digite o valor na posição [0.{contador1}]: ')))
#     contador1+=1
#     if contador1 >= 3:
#         matriz.append(posicoes[:])
#         posicoes.clear()
#         break
# for sequencia1 in range(3):
#     posicoes.append(int(input(f'Digite o valor na posição [1.{contador2}]: ')))
#     contador2+=1
#     if contador2 >=3:
#         matriz.append(posicoes[:])
#         posicoes.clear()
#         break
# for sequencia2 in range(3):
#     posicoes.append(int(input(f'Digite o valor na posição [2.{contador3}]: ')))
#     contador3+=1
#     if contador3 >=3:
#         matriz.append(posicoes[:])
#         posicoes.clear()
#         break
# # print(f'[   {matriz[0][0]}   ]   [   {matriz[0][1]}   ]   [   {matriz[0][2]}   ]\n[   {matriz[1][0]}   ]   [   {matriz[1][1]}   ]   [   {matriz[1][2]}   ]\n[   {matriz[2][0]}   ]   [   {matriz[2][1]}   ]   [   {matriz[2][2]}   ]')
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for esquerda in range(0,3):
    for direita in range(0,3):
        matriz[esquerda][direita]=int(input(f'Digite um valor na posição [{esquerda},{direita}]: '))
print('-='*60)
for quadros in range(0,3):
    for recheio in range(0,3):
        print(f'[{matriz[quadros][recheio]:^5}]',end='')
    print()