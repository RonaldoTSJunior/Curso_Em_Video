#Variáveis Compostas (LISTAS)
# -> Uma estrutura de lista contendo outra lista dentro. EX:
# dados=[]                #Também posso criar uma lista assim: dados=list()
# dados.append('Pedro')
# dados.append('25')
# print(dados[0])         #[0] Serve para imprimir a informação contida na lista na posição 0.
# pessoas=[]              #Crio uma nova lista que irá se tornar a variavel composta de listas.
# dados.append('Mario')   
# dados.append(25)
# dados.append('Joao')
# dados.append(32)
# pessoas.append(dados[:]) #Utilizando o fatiamento conseguimos criar uma cópia da lista DADOS dentro da lista pessoas sem conectar a lista original DADOS e a cópia em PESSOAS.
# print(pessoas)

# -> Imprimindo itens das listas e mostrando variaveis compostas.
# pessoas=[['pedro',25],['Mario',32],['Joao',45]]     #Desta forma é possível criar uma lista composta caso já possua os dados.
# print(pessoas[0][0])      #Utilizando dois [] é possível identificar o item que deseja imprimir! Sendo o primeiro [] pára escolher a lista, e o segundo o conteudo dentro da lista.
# print(pessoas[1][0])
# print(pessoas[2])
# print(pessoas[1][1])

# -> PARTE PRÁTICA DA AULA.
#Exemplo de cópia de lista conectadas, ou seja, tudo que for alterado na estrutura B será na A.
# teste=[]
# teste.append('Guanabara')
# teste.append(40)
# galera=[]
# galera.append(teste)     #Chamando a lista 'TESTE' para dentro da lista GALERA sem fatiamento [:], irá criar uma ligação entre as duas listas TESTE "original" e TESTE "dentro de galera".
# teste[0] = 'Maria'
# teste[1] = 25
# galera.append(teste)
# print(galera)            #Exemplo da ligação entre as listas! 

# -> EXEMPLO CORRETO PARA LISTA COMPOSTA.

# teste=[]
# teste.append('Guanabara')
# teste.append(40)
# galera=[]
# galera.append(teste[:])    #Adicionando o [:] dentro do append(TESTE) irá criar uma cópia da lista original que poderá ser alterada sem interferir na original.
# teste[0] = 'Maria'
# teste[1] = 25
# galera.append(teste)
# print(galera)              #Ao printar a lista galera poderá ver que a cópia da lista teste dentro de galera foi alterada, mas a original foi mantida!

# -> METODO MAIS SIMPLES PARA CRIAR LISTA COMPOSTA.
# galera=[['Mario',25],['Joao',32],['Patrick',45],['Nick',20]]
# print(galera[3][0])
# for pessoa in galera:        #Ao utilizar a estrutura FOR, é possível imprimir todas as listas dentro de GALERA individualmente.
#     #print(pessoa[0])        #Ao adicionar [0] estou pedindo para que imprima somente os itens de indice 0 presente nas listas. Também pode ser feito com indice [1] para puxar somente as idades.
#     galera.sort()            #.sort() Para deixar a impressão dos dados da lista em ordem  
#     print(f'{pessoa[0]} Tem {pessoa[1]} anos de idade.')          #Também é possível adicionar o format para personalizar o print.

# -> Listas compostas com laço de repetição + input do usuario
# galera=[]
# dados=[]
# for contador in range(3):
#     dados.append(str(input('Digite seu nome: ')).capitalize().strip())
#     dados.append(int(input('Digite sua idade: ')))
#     galera.append(dados[:])
#     dados.clear()              #Utiliza-se o clear, para limpar os dados anteriores de ''DADOS'' para então pode ser adicionado os inputs. Caso não seja utilizado o print da lista será impresso vazio.
# galera.sort()                  #Utilizar o .sort() fora do laço para ser executado depois de todo o laço, mas antes do print.
# print(galera)

# -> Laço if else para criar condições diferentes de print.
galera=[]
dados=[]
maior=menor=0         #Contador maior e menor idade.           #Este estrutura com variaveis posso somente fazer com variaveis simples!
for contador in range(3):
    dados.append(str(input('Digite seu nome: ')).capitalize().strip())
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()              
galera.sort()     
for pessoas in galera:
    if pessoas[1] >= 21:
        maior+=1
        print(f'{pessoas[0]} é maior de idade!')
    else:
        menor+=1
        print(f'{pessoas[0]} é menor de idade!')
print(f'Essa galera possui {maior} maiores de idade, e {menor} menores de idade!')