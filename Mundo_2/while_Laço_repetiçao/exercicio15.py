# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from time import sleep
print('-='*30)
print('{:^30}'.format('BANCO PY'))
print('-='*30)
sleep(1)
saque=int(input('Qual o valor que deseja sacar? R$'))
vlr_saque=saque                #Variavel contendo o valor de saque desejado pelo usuario, para poder ser utilizado no algoritmo.
contagem_cedula=0              #Variavel que será utilizada para contar quantas vezes a cédula foi utilizada
cedula=50                      #Começa recebendo o maior valor de cedula disponível, e representa os valores de cédulas.
while True:
    if vlr_saque >= cedula:    #Verifica se o valor atual de saque é maior ou igual a o valor da cédula atual. Se for ele executara o bloco de comando que está dentro do IF.
        vlr_saque-=cedula      #Comando que executara o calculo para retirada do valor atual da cédula do valor atual da variavel ''vlr_saque''.
        contagem_cedula+=1     #Adiciona ao contador de cédulas um ponto toda vez que o valor atual da cédula for subtraido do vlr_saque atual com sucesso.
    else:                                 #Bloco de código que executa se o bloco IF não for possível de executar.
        if contagem_cedula > 0:           #Impede de mostrar a contagem de cédulas que não foram utilizadas.
            print(f'Total de cédulas {contagem_cedula} de R${cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        contagem_cedula=0                 #Zera o valor da variavel para que o próximo valor possa ser contabilizado.
        if vlr_saque==0:                  #Se após verificar todas as cédulas restantes e o valor de saque for 0, encerra o programa.
            print('-='*30,"\nFinalizando...")
            break