# Crie um programa que leia 6 numeros inteiros, e mostre a soma somente daqueles que forem pares. Se for impar, desconsidere
s=0
for c in range(6):
    n=int(input('Digite um numero '))
    if n % 2==0:
        s+=n
print(f'A soma de seus números pares é {s}')