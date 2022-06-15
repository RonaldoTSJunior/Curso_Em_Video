#if...else / if... (Exemplos)

#EXEMPLO 1
#nome=str(input('Qual é o seu nome? '))
#if nome == 'Ronaldo':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é tão normal!')
#print(f'Bom dia, {nome}!')

#EXEMPLO 2
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print(f'A sua média foi {m:.1f}.')
#If else simplificado:
#print('PARABÉNS!'if m >=6 else 'ESTUDE MAIS!')

#if else composto:
if m >=6:
    print('Parabéns! Você passou.')
else:
    print('Desculpe! Não foi dessa vez.')


