# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
principal=[]
par=[]
impar=[]
user=0
for sequencia in range(7):
    user=int(input('Digite um valor: '))
    if user % 2 == 0:
        par.append(user)
        par.sort()
    else:
        impar.append(user)
        impar.sort()
principal.append(par[:])
principal.append(impar[:])
print(f'A lista contendo os valores pares ficou assim: {principal[0]}.\nE a lista contendo os valores impares ficou assim: {principal[1]}')