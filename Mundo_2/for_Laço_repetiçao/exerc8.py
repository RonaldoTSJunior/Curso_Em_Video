# crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços.
print('''
    ---------DETECTOR DE PALINDROMO---------
    ''')
frase=str(input('Digite uma frase ou palavra: ')).strip().lower()        #.strip() para remover os espaços da palavra digitada.
tamanho=len(frase)                                 #Cria variável para descobrir o tamanho da string.
invertido=''                          #Variável global para utilização no processo de inversão da string.
for letra in range(tamanho,0,-1):
    invertido+=frase[letra-1]          #Somando a var Invertido com frase. 
print(f'Sua frase invertida é {invertido}')
if frase==invertido:             #Cria a condição para  descobrir o resultado, no caso se é ou não um palindromo.
    print(f'É um palíndromo!')
else:
    print('Não é um palindormo')
