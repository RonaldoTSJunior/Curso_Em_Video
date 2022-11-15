def aumentar(m = 0, taxa = 0, formato=False):
    '''
    
    -> Função para aumentar o valor "paramêtro" na % desejada.
    
    :param formato: True = Formata o valor  -  False(PADRÃO) = Não formata o valor
    
    :param m: Receberá o valor que deverá ser aumentado.
    
    :param taxa: Recebe o valor especifícado em que deve aumentar o paramêtro M
    
    :return: Retorna o valor aumentado
    
    '''
    res = m + (m * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(m = 0, taxa = 0, formato=False):
    '''
    
    -> Função para diminuir o valor "paramêtro" na % desejada.
    
    :param formato: True = Formata o valor  -  False(PADRÃO) = Não formata o valor
    
    :param m: Receberá o valor que deverá ser diminuído.
    
    :param taxa: Recebe o valor especifícado em que deve diminuír o paramêtro M
    
    :return: Retorna o valor decrescido.
    
    '''
    res = m - (m * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(m = 0, formato=False):
    '''
    
    -> Função para dobrar o valor "paramêtro".
    
    :param formato: True = Formata o valor  -  False(PADRÃO) = Não formata o valor
    
    :param m: Receberá o valor que deverá ser dobrado.
    
    :return: Retorna o valor multiplicado por 2.
    
    '''
    res = m * 2
    return res if formato is False else moeda(res)


def metade(m = 0, formato=False):
    '''
    
    -> Função para cortar o valor "paramêtro" pela metade.
    
    :param formato: True = Formata o valor  -  False(PADRÃO) = Não formata o valor
    
    :param m: Receberá o valor que deverá ser cortado pela metade.
    
    :return: Retorna a metade do valor.
    
    '''
    res = m / 2
    return res if formato is False else moeda(res)


def moeda(m = 0.0, moeda = "R$",):
    '''
    
    -> Função para transformar o valor "Paramêtro" em formato de moeda.
    
    :param m: Receberá o valor que deverá ser transformado.
    
    :param moeda: Insere o R$ no Paramêtro. 
    
    :return: Retorna o valor transformado.
    
    '''
    
    return f"{moeda}{m:.2f}".replace(".",",")

        
def resumo(p = 0 , a = 50 , r = 20):
    print('-' * 30)
    print('RESUMO DE VALORES'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de redução: \t{diminuir(p, r, True)}')
    print('-' * 30)
