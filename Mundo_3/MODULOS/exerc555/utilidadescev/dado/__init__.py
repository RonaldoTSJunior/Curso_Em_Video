def leiadinheiro(msg):
    '''
    => Função para ler apenas valores monetários
    :param msg: recebe o valor digitado pelo usuário e faz a verificação se é apenas um valor monetário ou não.
    :return:    se for monetário, retorna o valor.
    '''
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",",".").strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)