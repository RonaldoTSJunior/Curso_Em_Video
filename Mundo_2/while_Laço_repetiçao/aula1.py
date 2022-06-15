n=1
par=impar=0
while n!=0:                     #cria condição para o programa rodar enquanto a condição não se cumprir
    n=int(input('Digite um valor: '))
    if n !=0:                   #condição para não contabilizar o 0 no calculo de par ou impar, e se a condição se cumprir, sai do loop.
        if n % 2 == 0:
            par+=1
        else:
            impar+=1
print(f'A quantia de números pares é {par} e a quantia de ímpares é {impar}')