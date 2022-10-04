#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
resultados=dict()
resultados['primeiro'] = random.randint(0,20)
resultados['segundo'] = random.randint(0,20)
resultados['terceiro'] = random.randint(0,20)
resultados['quarto'] = random.randint(0,20)
ordenado=sorted(resultados.values())
vencedor=max(ordenado)
for key,values in resultados.items():
    print(f'O {key} jogou {values}.')
if resultados['primeiro'] > resultados['segundo'] and resultados['primeiro'] > resultados['terceiro'] and resultados['primeiro'] > resultados['quarto']:
    print(f'O vencedor foi o * PRIMEIRO * jogador, seu número foi {vencedor}')
elif resultados['segundo'] > resultados['primeiro'] and resultados['segundo'] > resultados['terceiro'] and resultados['segundo'] > resultados['quarto']:
    print(f'O vencedor foi o * SEGUNDO * jogador, seu número foi {vencedor}')
elif resultados['terceiro'] > resultados['primeiro'] and resultados['terceiro'] > resultados['segundo'] and resultados['terceiro'] > resultados['quarto']:
    print(f'O vencedor foi o * TERCEIRO * jogador, seu número foi {vencedor}')
elif resultados['quarto'] > resultados['primeiro'] and resultados['quarto'] > resultados['segundo'] and resultados['quarto'] > resultados['terceiro']:
    print(f'O vencedor foi o * QUARTO * jogador, seu número foi {vencedor}')
print(f'Os números escolhidos em ordem ficaram assim: ',ordenado)