# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
from time import sleep
serieA=('Corinthians','Athletico PR','Palmeiras','Atlético-MG','Internacional','Coritiba','Fluminense','América-MG','São Paulo','Santos','Bragantino','Ceara SC','Botafogo','Flamengo','Goiás','Avaí','Cuiabá','Atlético-GO','Juventude','Fortaleza')
serieB=('Cruzeiro','Bahia','Vasco da Gama','Sport Recife','Grêmio','Operário','Novorizontino','Brusque','Criciúma','Tombense','CSA','Sampaio Corrêa','Ponte Preta','Londrina','Náutico','Chapecoense','CRB','Ituano','Vila Nova','Guarani')
print('-='*25)
print('Bem Vindo Ao Bom de Bola!')
print('-='*25)
sleep(1)
ordemalfa1=sorted(serieA)
ordemalfa2=sorted(serieB)
escolha=str(input('Escolha a série que deseja os dados. [A/B]: ')).upper().strip()
if escolha=='A':
    print('Você escolheu a série A!')
    print('Os 5 primeiros times da \033[35mSérie A\033[m são:',serieA[:6])
    print('Times em ordem alfabética:',ordemalfa1)
    print('O time da Chapecoense não está na Série A!')
elif escolha=='B':
    print('Você escolheu a série B!')
    print('Os 5 primeiros times da \033[32mSérie B\033[m são:',serieB[:6])
    print('Times em ordem alfabética:',ordemalfa2)
    print('A Chapecoense se encontra na posição:',serieB.index('Chapecoense'))
else:
    print('!ERROR! OPÇÃO INVÁLIDA.')
print('Finalizando...')
