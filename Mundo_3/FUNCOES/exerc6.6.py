# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#MINHA SOLUÇÃO:
# def ajuda(msg):
#     '''
#     => Função que utiliza do Interactive Help para buscar documentações de outras funções e/ou bibliotecas.
#     :param msg: Recebe o nome da função ou biblioteca a ser pesquisada.
#     '''
#     print('\033[0;0;47m=\033[m'*40)
#     print('     \033[0;0;47mSISTEMA DE AJUDA PyHELP\033[m')
#     print('\033[0;0;47m=\033[m'*40)
#     while True:
#         from time import sleep
#         comando = input(msg)
#         sleep(0.4)
#         if comando.upper() == 'FIM':
#             print('\033[0;0;43m=\033[m'*40)
#             print('     \033[0;0;43mADEUS E ATÉ A PRÓXIMA!!!\033[m')
#             print('\033[0;0;43m=\033[m'*40)
#             break
#         print('\033[0;0;44m=\033[m'*40)
#         print(f'   \033[0;0;44mACESSANDO SISTEMA DE AJUDA DE \033[m\033[0;33;44m{comando}\033[m')
#         print('\033[0;0;44m=\033[m'*40)
#         sleep(1)
#         a = help(comando)
        
        
# #Programa Principal:
# user = ajuda('Função ou Biblioteca: ')


#SOLUÇÃO GUANABARA:
from time import sleep

#Paleta de Cores
c = ('\033[m',        # 0 - sem cores 
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
    );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
    
    
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
    

#Programa Principal:
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)