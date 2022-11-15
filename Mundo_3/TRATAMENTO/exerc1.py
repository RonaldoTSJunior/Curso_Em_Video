# Reescreva a função leiaInt() que fizemos no desafio 104
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m!ERROR! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário não adicionou este número inteiro.\033[m')
            return 0
        else:
            return n
        
            
def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m!ERROR! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário não adicionou este número real.\033[m')
            return 0
        else:
            return r
        
        
#Programa Principal:
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro: \033[0;32m{n1}\033[m')
print(f'Você digitou o número real: \033[0;33m{n2}\033[m')