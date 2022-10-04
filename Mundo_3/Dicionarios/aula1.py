#Dicionários são identificados por '{ }'
#valores ou values é o conteúdo dentro dos dicionarios ou keys
#Ex: print(filmes.values()) vai me retornar somente os conteudos dentro da variavel Filmes.
#Ex²: print(filmes.keys()) vai me retornar os nomes dos dicionários ou 'Keys'.
#Ex³: print(filmes.items()) vai me retornar ambas as informações, os 'values' e as 'keys'.
#Exemplo no laço FOR:
#filmes={'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}  #Também é possível criar dicionários utilizando dict()
# for k,v in filmes.items():            #Com o for, é possível retornar ambas as informações de forma organizada conforme no exemplo.
#     print(f'O {k} é {v}')
# print(f'O {filmes["titulo"]} foi lançado em {filmes["ano"]}')     #Printando informações específicas com um print formatado.
#del filmes['ano']         #Comando Del seguido da especificação, serve para deletar aquela key juntamente com seu conteudo.
#filmes['titulo'] = 'Matrix'      #Nos dicionários, é possível a modificação dos valores.
#filmes['nota'] = 10             #Podemos adicionar mais Keys em nosso dicionário, apenas criando-a e atribuindo seu valor.
#print(filmes)
#Exemplo de dicionário dentro de uma lista:
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())      #Ao invés de utilizar o fatiamento [:] para inserir as informações na lista, utilizamos '.copy()' para inserir as keys e os values do dicionarios dentro da lista.   
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()
    