# Aprimore o desafio 93 para que ele funcione com vários jogadores
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
equipe = dict()
partidas = list()
while True:
    equipe.clear()
    equipe['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    total = int(input(f'Quantas partidas {equipe["nome"]} jogou?: '))
    partidas.clear()
    for contador in range(0,total):
        partidas.append(int(input(f'    Quantos gols na partida {contador}? ')))
    equipe['gols'] = partidas[:]
    equipe['total'] = sum(partidas)
    time.append(equipe.copy())
    while True: 
        escolha = str(input('Deseja continuar? [S/N]: ')).upper()[0].strip()
        if escolha in 'SN':
            break
        print('!ERROR! Digite apenas S ou N.')
    if escolha == 'N':
        break
print('-='*45)
print('Cód     ', end='')
for key in equipe.keys():
    print(f'{key:<15}', end='')
print()
print('-'*45)
for key, values in enumerate(time):
    print(f' {key:>3} ', end='')
    for dados in values.values():
        print(f' {str(dados):<15}', end='')
    print()
print('-'*45)
while True:
    search = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if search == 999:
        break
    if search >= len(time):
        print(f'!ERROR! Não existe jogador com o código {search}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR * {time[search]["nome"]} *:')
        for codigo, gols in enumerate(time[search]["gols"]):
            print(f'   No jogo {codigo+1} fez {gols} gols.')
    print('-'*45)
print('<<<<< VOLTE SEMPRE! >>>>>')