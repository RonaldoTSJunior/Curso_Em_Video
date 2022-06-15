#Nesta aula foi ensinado a utilizar a estrutura BREAK, ele serve para interromper um laço no meio do caminho.
n=s=c=0
while True:
    n=int(input('Digite um número: '))
    c+=1
    if n==999:
        break
    s+=n
print(f'A soma de seus números é {s}\nE a quantia de números digitados foi {c}')
