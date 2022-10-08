# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
#MINHA SOLUÇÃO DO EXERCICIO:
#Iniciei a variavel ESCOLHA para uso dentro do while:
escolha = 0

#Função que executa o contador:
def contador(inicio, fim, passo):
  if passo < 0:
    passo *= -1
  if passo == 0:
    passo = 1
  sleep(1)
  print('PROCESSANDO...')
  print(f'SUA CONTAGEM PERSONALIZADA DE {inicio} ATÉ {fim} DE {passo} EM {passo} ⤵')
  if inicio < fim:
      cont = inicio
      while cont <= fim:
          print(f'{cont}  ', end='',flush=True)
          sleep(0.5)
          cont+=passo
      print('FIM!')
  else:
      cont = inicio
      while cont >= fim:
          print(f'{cont}  ', end='',flush=True)
          sleep(0.5)
          cont-=passo
      print('FIM!')
      
#TITULO E MENU DE OPÇÕES:      
print('INICIANDO SISTEMA, POR FAVOR AGUARDE...')
sleep(1)
print('''
      BEM VINDO AO CONTADOR!
      [1] PARA CONTAR DE 1 ATÉ 10 DE 1 EM 1
      [2] PARA CONTAR DE 10 ATÉ 0 DE 2 EM 2
      [3] PARA PERSONALIZAR SEU CONTADOR
      [4] PARA FECHAR O PROGRAMA
      ''')


while True:
  while True:
    escolha = int(input('DIGITE O CÓDIGO DA OPÇÃO DESEJADA: '))
    if escolha in [1,2,3,4]:
      break
    print('!ERROR! OPÇÃO INVÁLIDA, SELECIONE APENAS ENTRE AS OPÇÕES DO MENU.')
  sleep(1)
  print('PROCESSANDO...')
  if escolha == 1:
    print('SUA CONTAGEM DE 1 ATÉ 10 DE 1 EM 1⤵')
    for counter in range(1,11,1):
      print(f'  {counter}', end='')
    print()
  elif escolha == 2:
    print('SUA CONTAGEM DE 10 ATÉ 0 DE 2 EM 2 ⤵')
    for counter in range(10,-1,-2):
      print(f'  {counter}', end='')
    print()
  elif escolha == 3:
        print('ATENÇÃO! DIGITE APENAS NÚMEROS INTEIROS NA PERSONALIZAÇÃO.')
        contador_inicio = int(input('Digite o número que deseja começar a contagem: '))
        contador_fim =int(input('Digite até que número deseja a contagem: '))
        contador_passo = int(input('Digite como será feita a contagem (Ex: 1 em 1, 2 em 2): '))
        contador(contador_inicio,contador_fim,contador_passo)
  elif escolha == 4:
    print('<<<< Finalizando Sistema... >>>>')
    sleep(1)
    break
#----------------------------------------------------------------------------------------------------------------
#                                                  FIM
#SOLUÇÃO GUANABARA:
# def contador(inicio,fim,passo):
#     if passo < 0:
#       passo *= -1
#     if passo == 0:
#       passo = 1
#     sleep(1)
#     print('PROCESSANDO...')
#     print(f'SUA CONTAGEM PERSONALIZADA DE {inicio} ATÉ {fim} DE {passo} EM {passo} ⤵')
#     if inicio < fim:
#         cont = inicio
#         while cont <= fim:
#             print(f'{cont}  ', end='',flush=True)
#             sleep(0.5)
#             cont+=passo
#         print('FIM!')
#     else:
#         cont = inicio
#         while cont >= fim:
#             print(f'{cont}  ', end='',flush=True)
#             sleep(0.5)
#             cont-=passo
#         print('FIM!')


# #Programa Principal:
# contador(1,10,1)
# contador(10,0,2)
# print('-='*20)
# print('Agora é a SUA vez de personalizar a contagem!')
# ini = int(input('Início:   '))
# fim = int(input('Fim:      '))
# pas = int(input('Passo:    '))
# contador(ini,fim,pas)
