# Escreva um programa que leia um número inteiro qualquer, e peça para o usuário escolher qual será a base de conversão:
# 1 para binário 
# 2 para octal 
# 3 para hexadecimal
escolha='s'
while escolha=='s':
    print('''
---------CONVERSOR DE NÚMEROS---------
* ESCOLHA A BASE PARA A CONVERSÃO *
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
''')
    numero=int(input('Digite seu número: '))
    base=int(input('Escolha sua base de conversão: '))
    if base==1:
        print(f'Conversão para BINÁRIO.\nSeu número BINÁRIO é: {bin(numero)}')
    elif base==2:
        print(f'Conversão para OCTAL.\nSeu número OCTAL é: {oct(numero)}')
    elif base==3:
        print(f'Conversão para HEXADECIMAL.\nSeu número HEXADECIMAL é: {hex(numero)}')
    else:
        print('!!!ERROR!!!\n OPÇÃO INVÁLIDA ')
    escolha=str(input('DESEJA REFAZER A OPERAÇÃO?\n[S/N]  '))