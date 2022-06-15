print('CARREGANDO PROGRAMA...')
print('A velocidade máxima da via é 80km/h. ')
v=int(input('Em qual velocidade se encontra o carro? '))
if v >80:
    print('Ultrapassou o limite de velocidade, você foi multado!')
    print(f'O valor da sua multa é R${(v-80)*7}. ')
else:
    print('BOA VIAGEM! DIRIJA COM CAUTELA.')


