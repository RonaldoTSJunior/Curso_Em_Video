#Crie um programa que leia o nome completo de uma pessoa e mostre separadamente o primeiro e ultimo nome.
n=str(input('Digite o seu nome: ')).upper().strip()
nome=n.split()
print(f'O seu primeiro nome é {nome[0]} ')
print(f'O seu segundo nome é {nome[len(nome)-1]} ')