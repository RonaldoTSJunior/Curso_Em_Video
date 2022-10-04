# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (somente se possuir ctps).
#idade para aposentadoria 65 anos.
#-----------------------------------------------------------------------------------------------------------------------
#SOLUÇÃO RONALDO:
# trabalho=dict()
# trabalho['nome'] = str(input('Nome: ')).capitalize().strip()
# trabalho['nascimento'] = int(input('Ano de Nascimento: '))
# trabalho['idade'] = 2022 - trabalho['nascimento']
# trabalho['ctps'] = int(input('Carteira de trabalho (Digite 0 caso não possua): '))
# if trabalho['ctps'] != 0:
#     trabalho['contratação'] = int(input('Ano de contratação: '))
#     trabalho['salário'] = float(input('Salário: R$'))
#     trabalho['aposentadoria'] = trabalho['idade'] + ((trabalho['contratação'] + 35) - 2022)
# print('-='*35)
# for key,values in trabalho.items():
#     print(f'• {key} - {values}')
#-----------------------------------------------------------------------------------------------------------------------
#SOLUÇÃO COM LIBRARY DATETIME:
from datetime import datetime
trabalho = dict()
trabalho['nome'] = str(input('Nome: ')).capitalize().strip()
nascimento = int(input('Ano de nascimento: '))
trabalho['idade'] = datetime.now().year - nascimento
trabalho['ctps'] = int(input('Carteira de trabalho (Digite 0 caso não possua): '))
if trabalho['ctps'] != 0:
    trabalho['contratação'] = int(input('Ano da contratação: '))
    trabalho['salário'] = float(input('Salário: R$'))
    trabalho['aposentadoria'] = trabalho['idade'] + ((trabalho['contratação'] + 35)- datetime.now().year)
print('-='*35)
for key,values in trabalho.items():
    print(f'• {key} - {values}')