# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo. 
while True:
    numero=int(input('Digite um número: '))
    print('-='*25)
    if numero <0:
        break
    for tabuada in range(0,11):
        print(f'{numero} x {tabuada} = {numero*tabuada}')
    print('-='*25)
print('Finalizando...')