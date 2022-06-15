# Crie um programa que leia duas notas de um aluno, calcule sua média, e mostre uma mensagem no final de acordo com a média atingida 
# media abaixo de 5 - reprovado 
# media entre 5 e 6.9 - recuperação 
# media acima de 7 - aprovado
escolha='s'
while escolha=='s':
    nome=str(input('NOME DO ALUNO: ')).capitalize()
    n1=float(input('Digite a primeira nota: '))
    n2=float(input('Digite a segunda nota: '))
    m=(n1+n2)/2
    if m>7:
        print(f'PARABÉNS {nome}! Sua média foi de {m}, você foi aprovado! ')
    elif m>5 and m<6.9:
        print(f'Sua média foi de {m}, está de recuperação {nome}! BOM ESTUDO. ')
    else:
        print(f'Sua média foi de {m}, infelizmente está reprovado {nome}! ')
    escolha=str(input('Deseja repetir o programa? s/n  ')).lower()