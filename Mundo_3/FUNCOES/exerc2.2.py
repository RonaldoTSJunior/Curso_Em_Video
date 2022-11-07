#  Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular 
# e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    '''
    => Função Para Cálculo Fatorial
    :param n: Coleta o número para fazer o cálculo fatorial.
    :param show: Valor lógico para mostrar ou não o cálculo até o resultado (PADRÃO 'FALSE').
    :return: Retorna o resultado do Cálculo Fatorial de N.
    '''
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*=cont
    return f


#Programa principal:
print(fatorial(5, show=True))
help(fatorial)