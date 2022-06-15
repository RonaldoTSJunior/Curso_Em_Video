# Crie um programa que leia o ano de nascimento de um atleta e informe sua categoria com base em sua idade 
# até 9 anos - mirim 
# até 14 anos - infantil 
# até 19 anos - junior 
# até 20 anos - senior 
# acima de 20 anos - master 
novamente='s'
while novamente=='s':
    print('BEM VINDO AO CENTRO DE TREINAMENTO DE SEREIOS.\n.\n.\n.\nSISTEMA CARREGANDO, POR FAVOR AGUARDE...')
    nascimento=int(input('Digite seu ano de nascimento: '))
    idade_atual=2022-nascimento
    if idade_atual<=9:
        print(f'Você tem {idade_atual} anos, entrou na categoria \33[1;30;40m[Mirim]\33[m PARABÉNS.')
    elif idade_atual>9 and idade_atual<=14:
        print(f'Você tem {idade_atual} anos, entrou na categoria \33[1;33;40m[infantil]\33[m PARABÉNS.')
    elif idade_atual>14 and idade_atual<=19:
        print(f'Você tem {idade_atual} anos, entrou na categoria \33[1;31;40m[Junior]\33[m PARABÉNS.')
    elif idade_atual>19 and idade_atual<=20:
        print(f'Você tem {idade_atual} anos, entrou na categoria \33[1;35;40m[Senior]\33[m PARABÉNS.')
    else:
        print(f'Você tem {idade_atual}, e se enquadra na categoria \33[1;36;40m[MASTER]\33[m PARABÉNS.')
    novamente=str(input('DESEJA REFAZER O TESTE?\n S/N  ')).lower()