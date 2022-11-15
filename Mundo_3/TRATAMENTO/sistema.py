# Vamos criar um menu em Python, usando modularização.
#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema vai ter 2 opções: Cadastrar uma nova pessoa e lista todas as pessoas cadastradas.
from lib.menu import*
from lib.arquivo import*
from time import sleep


arq = 'menuinterativo.txt'


if not arquivoExiste(arq):
    criarArquivo(arq)
    
    
#Programa Principal:


while True:
    resposta = menu(["Acessar Cadastros","Cadastrar Novas Pessoas","Sair do Sistema"])
    if resposta == 1:
        #Opção de listar todo conteúdo do arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de adicionar novas pessoas ao arquivo.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção para sair do sistema.
        cabecalho('      \033[0;36mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabecalho('\033[0;31m!ERROR! OPÇÃO INVÁLIDA\033[m')
    sleep(2)