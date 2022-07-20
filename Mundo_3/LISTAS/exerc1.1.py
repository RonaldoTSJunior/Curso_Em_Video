# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados=[]
inicial=[]
escolha='s'
maior=menor=0
while escolha == 's':
    inicial.append(str(input('Digite um nome: ')).capitalize().strip())
    inicial.append(float(input('Digite o peso: ')))
    escolha=str(input('Deseja continuar? [S/N]: ')).lower().strip()
    if len(dados) == 0:
        maior=menor=inicial[1]
    else:
        if inicial[1] > maior:
            maior=inicial[1]
        if inicial[1] < menor:
            menor=inicial[1]
    dados.append(inicial[:])
    inicial.clear()
    print('='*60)
print('='*60)
print(f'-> Ao todo foram cadastradas {len(dados)} pessoas.\n-> O maior peso no grupo é de {maior}kg.\n-> O menor peso no grupo é de {menor}kg.')
print('='*60)
