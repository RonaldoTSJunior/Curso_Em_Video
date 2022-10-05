# # Crie uma função que recebe uma lista denúmeros e:
# # a.retorne o maior elemento
# # b.retorne a soma dos elementos   *
# # c.retorne o número de ocorrências do primeiro elemento da lista  *
# # d.retorne a média dos elementos  *
# # e.retorne o valor mais próximo da média dos elementos
# # f.retorne a soma dos elementos com valor negativo  *
# # g.retorne a quantidade de vizinhos iguais
principal=[]
media=[]
maior,prox,soma,iguais,contador=0
while True:
    user=int(input('Digite um valor: '))
    if user not in principal:
        principal.append(user)
    elif user in principal:
        iguais+=1
        
    contador+=1
    soma+=user
    escolha=str(input('Deseja continuar? [S/N]: ')).strip()
    if escolha in 'Nn':
        break
    
media=soma/len(principal)
maior=max(principal)
lista_ordenada = sorted(principal)
tamanho_lista=len(lista_ordenada)
numero_proximo = 0,0

for prox in lista_ordenada:
    if prox <= media:
        numero_proximo = prox
print('Lista escolhida: ',sorted(principal))
print(f'A soma dos elementos da lista é: {soma}.\nA soma negativa é: {soma*-1}.\nA média dos elementos da lista é: {media:.1f}.\nO primeiro elemento da lista [{principal[0]}], se repete {principal.count(principal[0])} vezes!\nO maior elemento na lista é {maior}!\nO elemento mais próximo a media da lista é: {numero_proximo}!\nA quantia de números vizinhos iguais é de: {iguais}')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
