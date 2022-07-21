# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz=[]
pares=0
linha2=[]
soma_coluna=0
for linha in range(0,3):
    lista=[]
    for coluna in range(0,3):
        aleatorios=int(input(f'Digite o valor na posição [{linha},{coluna}]: '))
        lista.append(aleatorios)
        if aleatorios % 2 == 0:
            pares+=aleatorios
        if coluna == 2:
            soma_coluna+=aleatorios
        if linha == 1: 
            linha2+=[aleatorios]
            maior=max(linha2)
    matriz.append(lista)
print('-='*60)          
print('A soma de todos os valores pares é:',pares)
print('A soma dos valores na terceira coluna é:',soma_coluna)
print('E o maior valor na segunda linha é:',maior)
print('-='*60)
for quadros in range(0,3):
    for recheio in range(0,3):
        print(f'[{matriz[quadros][recheio]:^5}]',end='')
    print()