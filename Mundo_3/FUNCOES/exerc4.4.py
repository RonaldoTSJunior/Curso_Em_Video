# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    '''
    => FUNÇÃO PARA RECEBER UM INPUT DE NÚMERO INTEIRO.
    :param msg: Recebe o número inteiro como string.
    :param ok: PADRÃO FALSE - Se for um número válido fica TRUE
    :param valor: Recebe a string contendo o número e converte para inteiro
    :return: Retorna o valor digitado se for válido.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m!ERROR! DIGITE UM NÚMERO INTEIRO!\033[m')
        if ok:
            break
    return valor

#Programa Principal:
numero = leiaInt('Digite um número: ')
print(f'Você digitou acabou de digitar o número {numero}')
help(leiaInt)