# Faça um programa que leia o ano de nascimento de um jovem, e de acordo com sua idade diga:
# se ele ainda vai se alistar ao exercito
# se já chegou a hora dele se alistar
# se já passou do tempo dele se alistar 
# Seu programa também deverá mostrar o tempo que falta ou quanto já passou para se alistar.
print('BEM VINDO AO ALISTAMENTO MILITAR!\n.\n.\n.')
novamente='s'
while novamente=='s':
    nascimento=int(input('Digite sua ano de nascimento: '))
    idade_atual=2022-nascimento
    idade_limite=18-idade_atual
    if idade_atual>18:
        print(f'Você tem {idade_atual}, e já passou {abs(idade_limite)} anos de se alistar.\nTalvez seja bom checar se esta tudo em ordem com o serviço militar.')
    elif idade_atual==18:
        print(f'Sua hora chegou, você completou {idade_atual}! Apresente-se para o alistamento militar na junta mais próxima!')
    else:
        print(f'Calma, você tem {idade_atual} ainda faltam {idade_limite} para seu alistamento.')
    novamente=str(input('Deseja fazer o teste novamente?\ns/n  ')).lower()