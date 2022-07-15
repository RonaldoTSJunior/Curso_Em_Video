# #VARIÁVEIS COMPOSTAS (LISTAS)
# #Listas podem ser modificadas, e server para guardar diversos elementos.
# COMANDOS
#lista.append() serve para adicionar itens ao final da lista
#lista.insert() serve para adicionar o item na posição desejada, EX: lista.insert(0,'pizza') na posição 0 quero inserir PIZZA. A pizza entrará na posição 0 da lista, e o restante avançará 1 posição sem eliminar nada.
#del lista[] serve para apagar o objeto na posição desejada
#lista.pop() serve normalmente para remover o ultimo objeto da lista, mas pode ser utilizado para remover objetos do parametro desejado.
#lista.remove('') serve para remover o objeto pelo nome/conteudo da posição.
#lista.sort() organiza em ordem minha lista. Ex: 5 6 7 8 9 10
#lista=list(range(4,11)) irá criar uma lista de números inteiros de 4 até 10 (excluido o ultimo sempre que no caso é o 11.)
#lista.sort(reverse=True) irá organizar minha lista em ordem inversa. Ex: 10 9 8 7 6 5
#len(lista) serve para mostrar o tamanho da lista, a quantia de posições partindo do 0 até o ultimo elemento.
#------------------------------------------------------------------------------------------------------------------------------------------
#PRÁTICA DA AULA
# num=[1,2,3,4,5]
# num[3]=8             # Substituir elemento dentro da lista por outro.
# num.append(19)        # Adicionar novo elemento ao final da lista.
# num.sort()            # Colocar a lista em ordem
# num.sort(reverse=True) # Colocar a lista em ordem, porém invertendo a mesma.
# num.insert()          # Serve para inserir valores na lista especificando a posição.
# num.pop()            # Serve para remover o elemento do indice desejado, ou remover apenas o ultimo elemento da lista.
# num.remove()         # Serve pra remover o elemento do indice indicado.
# print(f'Essa lista possui {len(num)} elementos!')    # Me retornará o tamanho desta lista
# # Exemplo de remoção de item usando laços de repetição:
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não localizado!')
#----------------------------------------------------------------------------------------------------------
# valores=[]
# for posicao in range (0,5):
#     valores.append(int(input('Digite um valor: ')))

# for posicao,valor in enumerate(valores):
#     print(f'Encontrei na posição: {posicao} o valor: {valor}!')
# print('Programa finalizado...')
#----------------------------------------------------------------------------------------------------------
a=[2,3,4,7]
b=a
b=a[:]                       # Utilizando o fatiamento, é possível adicionar somente uma cópia da lista A na variável B sem criar a ligação entre elas.
b[2]=8                       # Quando igualo uma lista a outra, crio uma ligação entre duas listas. Então uma alteração feita em uma é feita na outra automaticamente. 
print(f'Lista A: {a}')
print(f'Lista B: {b}')