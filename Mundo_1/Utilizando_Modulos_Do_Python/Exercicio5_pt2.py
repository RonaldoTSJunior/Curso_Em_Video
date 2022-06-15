#Crie um programa que leia um nome pelo teclado e mostre:
#Quantas vezes aparece a letra ''A''
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

nome=str(input('Digite um nome: ')).upper().strip()
print('Analisando o nome. . .')
print(f'A letra A aparece {nome.count("A")} vezes ')
print(f'A posição em que a letra "A" aparece a primeira vez é {nome.find("A")+1} ')
print(f'A posição em que a letra "A" aparece a ultima vez é {nome.rfind("A")+1} ')
