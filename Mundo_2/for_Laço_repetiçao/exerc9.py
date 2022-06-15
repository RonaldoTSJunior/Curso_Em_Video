# crie um programa que leia a data de nascimento de 7 pessoas, e diga quantas ainda não atingiram a maioridade e quantas ja atingiram
from time import sleep
print('''
---------DETECTOR DE MAIORIDADE---------
Por favor, aguarde um momento!
.
.
.
''')
sleep(1)
contador_maior=0
contador_menor=0
for nascimento in range(0,7,1):
    nome=str(input('Digite seu primeiro nome: ')).capitalize()
    ano=int(input('Digite seu ano de nascimento: '))
    idade=2022-ano
    maior_idade=18
    if idade > maior_idade:
        contador_maior+=1
        print(f'''
        {nome} possui \033[35m{idade}\033[m anos!
        Parabéns!
        Você já atingiu a maior idade!
        ''')
    elif idade < maior_idade:
        contador_menor+=1
        print(f'''
        {nome} possui \033[35m{idade}\033[m anos!
        Puxa! 
        Parece que você ainda não atingiu a maior idade.
        Faltam ainda {maior_idade-idade} anos
        ''')
print(f'''
{contador_maior} Pessoas possuem maioridade
{contador_menor} Pessoas não possuem maioridade
''')