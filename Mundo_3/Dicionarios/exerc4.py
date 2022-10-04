# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
equipe = dict()
equipe['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {equipe["nome"]} jogou?: '))
equipe['totais'] = 0
gol=[]
for quant in range(0,partidas,1):
    gols = int(input(f'Quantos gols na partida {quant}? '))
    gol.append(gols)
    equipe['gols'] = gol
    equipe['totais'] += gols
print(equipe)
print('-='*36)
for key,values in equipe.items():
    print(f'O campo {key} tem valor {values}')
print('-='*36)
print(f'O jogador {equipe["nome"]} jogou {partidas} partidas.')
for indice,values in enumerate(equipe["gols"]):
    print(f'     => Na partida {indice}, fez {values} gols.')
print(f'Foi um total de {equipe["totais"]} gols')