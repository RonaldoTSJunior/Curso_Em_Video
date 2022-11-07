#INTERACTIVE HELP:

#Utilizando a função interna help(), é possível pesquisar sobre documentações de library's ou funções internas sem sair do vs code! Basta digitar o comando abaixo, e dar play!
#help()
#Também é possível receber a documentação de um objeto em especifíco, por exemplo: help(print), irá me retornar a documentação da função interna print.
#Outro exemplo é quando desejo saber os parametros de uma função, exemplo:
#print(input.__doc__)   #chamando o .__doc__ eu recebo a documentação daquela função!


#DOCSTRINGS:
#De forma resumida, é uma string de documentação. Ela serve para documentar funções e quando for chamado com o help(função), irá mostrar como funciona a função!
#Um exemplo com uma função criada pelo usuário:
# def contador(i,f,p):
#     #Docstring começa com ''' e finaliza com ''', escrevendo assim entre as aspas simples.
#     '''
#     -> FAZ UMA CONTAGEM PRÉ DETERMINADA E MOSTRA NA TELA
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: Sem retorno
#     '''
#     cont=i
#     while cont <= f:
#         print(f' {cont} ', end='..')
#         cont += p
#     print(' FIM !!!')
# contador(2,10,2)
# help(contador)



#PARÂMETROS OPCIONAIS:
# def somar(a=0, b=0, c=0):      # Como está declarado 3 parâmetros, caso na chamada abaixo não contenham 3 parâmetros, vai dar erro no programa. Sendo assim, colocamos a, b ou c=0 para o caso de não receber nenhuma informação ele receberá o valor 0.
#     '''
#     -> Executa a soma dos três valores informados.
#     :param a: O primeiro valor
#     :param b: O segundo valor
#     :param c: O terceiro valor
#     Função criada em estudos por Ronaldo Junior.
#     '''
#     s = a+b+c
#     print(f'A soma vale {s}')
    
# somar(3, 2, 5)
# somar(8, 4)
# somar()
# help(somar)



#ESCOPO DE VARIÁVEIS:
# def teste():
#     x = 8     # A variável X é uma variável LOCAL, pois existe apenas dentro da função.
#     print(f'Na função teste, o N vale {n}') # Mesmo a variável N sendo definida depois, o função ainda sim pode receber o valor atribuido após a função. Basta chamar a função após a definição do value.
#     print(f'Na função teste, o X vale {x}')
# #Programa Principal:
# n = 2     # Uma variável global é declarada (criada) fora das funções e pode ser acessada por todas as funções presentes no módulo onde é definida.
# teste()
# print(f'No programa principal, o N vale {n}')


# def teste(b):
#     global a        # Apagaria o espaço novo criado para a Var local A, e substitui o A = 5 global por A = 8 GLOBAL (SEM MODIFICAR O VALOR DA VAR 'A' GLOBAL.).
#     a = 8           # Mesmo criando a mesma variável com valor diferente, ela se torna LOCAL e não interfere com a variável 'A' GLOBAL .                  
#     b += 4          # A variável A LOCAL, não interfere com a soma! Pois é criada uma variável LOCAL para armazenar o A.
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')    
   
    
# a = 5
# print(f'A fora vale {a}')          
# teste(a)


# def funcao():     
#     n1 = 4                   # Var Local
#     print(f'N1 LOCAL vale {n1}')
#
#
# n1 = 2                       # Var Global
# funcao()
# print(f'N1 GLOBAL vale {n1}')


#RETORNANDO VALORES:
#Exemplo:
# def somar(a = 0, b = 0, c = 0):
#     s = a + b + c
#     return s
# #Programa Principal:
# r1 = somar(3,2,5)
# r2 = somar(2,2)
# r3 = somar(6)
# print(f'Meus cálculos deram {r1} - {r2} - {r3}.')


#PRÁTICA DA AULA:


#Exemplo 1:
# def fatorial(num = 1):
#     f = 1
#     for cont in range(num, 0, -1):
#         f *= cont
#     return f
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Meus resultados foram | {f1} | {f2} | {f3} |')


#Exemplo 2:
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# num = int(input('Digite um número: '))
# if par(num):
#     print('É par!')
# else:
#     print('É impar!')