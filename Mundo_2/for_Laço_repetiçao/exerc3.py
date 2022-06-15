# faça um programa que calcule a soma entre todos os número impares, e multiplos de 3 que se encontram no intervalo de 1 e 500
s=0
for i in range(1,501):
    if i % 2!=0:
        if i % 3==0:
            s+=i
print(f'A soma dos números impares e multiplos de 3 são {s}')
