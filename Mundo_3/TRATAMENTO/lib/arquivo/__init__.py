from lib.menu import *

def arquivoExiste(nome):
    try:
        a = open(nome, "r")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def criarArquivo(nome):
    try:
        a = open(nome, "a+")
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, "r")
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()    
        
def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escriva dos dados!')    
        else:
            print(f'Novo registro de < {nome} > adicionado com sucesso!')
            a.close() 