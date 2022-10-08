#Def significa DEFINIR FUNÇÕES, onde você cria uma rotina de algo, ou seja, cria uma função não existente nativamente no python.
#Ex: ao inves de executar 6 print() exatamente iguais, posso criar uma def para isso.
# def mostralinha():
#     print('-'*30)
    
        
# #Programa Principal
# mostralinha()
# print('CURSO EM VIDEO')
# mostralinha()
# print('GUSTAVO GUANABARA')
# mostralinha()
# print('APRENDA PYTHON')
# mostralinha()
#---------------------------------------------------------------------------------------
#Def com mensagem:
# def titulo(txt):
#     print('-'*40)
#     print(txt)
#     print('-'*40)
    
    
# #Programa principal
# titulo('CURSO EM VIDEO')
# titulo('APRENDA PYTHON')
# titulo('GUSTAVO GUANABARA')
#---------------------------------------------------------------------------------------
#Parte Prática da Aula:
#Criar função que soma parametros já definidos, e mostra na tela.
# def soma(a,b):
#     print(f'A = {a} B = {b}')
#     s = (a + b)
#     print(f'A soma {a} + {b} = {s}')
    
#Programa Principal
# soma(a=7,b=15)     #Podemos escolher a ordem dos parametros, contanto que fique explicito.
#----------------------------------------------------------------------------------------
#Empacotamento de funções (Utilizando Tuplas):
# def contador(*num):            #O '*' dentro dos () significa DESEMPACOTAR, e é usado quando não se sabe quantos parametros serão adicionados à função.
#    tam = len(num)
#    print(f'Recebi os valores {num} que são ao todo {tam} números.')
            
# #Programa Principal
# contador(5, 4, 2, 10)
# contador(8, 6, 9)
# contador(2, 1)
#----------------------------------------------------------------------------------------
#Empacotamento de funções (Utilizando Listas):
# def dobra(lst):
#     pos=0
#     while pos < len(lst):
#         lst[pos]*=2
#         pos+=1
#     print(f'A sua lista é {valores} e com seus valores dobrados fica: {lst}')
    
    
# #Programa Principal
# valores=[7,2,5,8,4]
# dobra(valores[:])