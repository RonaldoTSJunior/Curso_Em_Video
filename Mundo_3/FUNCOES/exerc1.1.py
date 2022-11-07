#  Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(nascimento):
    from datetime import date
    print('='*40)
    idade = date.today().year - nascimento
    if idade >= 18 and idade <=64:
        return f'Tem {idade} anos, portanto o voto é OBRIGATÓRIO'
    elif idade < 18 and idade >= 16 or idade > 65:
        return f'Tem {idade} anos, portanto o voto é OPCIONAL'
    elif idade < 16:
        return f'Tem {idade} anos, portanto o voto é NEGADO'
    

#Programa principal    
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))