# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
todos=[]
pares=[]
impares=[]
escolha='s'
while escolha == 's':
    user=int(input('Digite um valor: '))
    todos.append(user)
    escolha=str(input('\033[41mDeseja continuar?\033[m [S/N]: ')).lower().strip()
    if escolha == 'n':
        for lista in todos:
            if lista % 2 == 0:
                pares.append(lista)
            elif lista % 2 != 0:
                impares.append(lista)
todos.sort()
pares.sort()
impares.sort()    
print('Sua lista de números ficou assim:',todos)
print('Sua lista de números pares ficou assim:',pares)
print('Sua lista de números impares ficou assim:',impares)