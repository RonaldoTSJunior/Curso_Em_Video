# desenvolva um programa que leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão
primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
n=int(input('Quantos elementos vamos exibir? '))
ultimo=primeiro+(n-1)*razao
ultimo=ultimo+1
for c in range(primeiro,ultimo,razao):
    print(c)
