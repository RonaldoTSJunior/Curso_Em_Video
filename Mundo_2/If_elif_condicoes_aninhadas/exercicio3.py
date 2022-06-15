# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela as seguintes mensagens:
# o primeiro valor é maior
# o segundo valor é maior
# Não existe valor maior, os dois são iguais
escolha='s'
while escolha=='s':
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    if n1>n2:
        print('O valor do primeiro número é maior que o segundo! ')
    elif n1<n2:
        print('O valor do segundo número é maior que o primeiro! ')
    else:
        print('Não existe valor maior, os dois são iguais! ')
    escolha=str(input('Deseja repetir? s/n  ')).lower()