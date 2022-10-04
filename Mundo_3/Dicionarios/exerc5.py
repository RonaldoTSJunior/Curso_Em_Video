# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        pessoa['sexo'] = str(input('Genêro [M/F]: ')).upper()[0].strip()
        if pessoa['sexo'] in 'MF':
            break
        print('!ERROR! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if escolha in 'SN':
            break
        print('!ERROR! Digite apenas S ou N')
    if escolha == 'N':
        break
media = soma / len(galera)
print('-='*35)
print(f'A)Tem {len(galera)} pessoas')
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'* {p["nome"]} - ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for key,values in p.items():
            print(f'{key} = {values}; ',end='')
        print()
print('<<<<<ENCERRADO>>>>>')