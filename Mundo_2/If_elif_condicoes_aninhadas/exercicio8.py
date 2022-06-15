# Crie uma logica que leia o peso e altura de uma pessoa e calcule seu imc(indice massa corporea), e mostre seu status de acordo com a tabela abaixo
# abaixo de 18.5 - abaixo do peso 
# entre 18.5 e 25 - peso ideal 
# 25 a 30 - sobrepeso 
# 30 a 40 - obesidade 
# acima de 40 - obesidade morbida
escolha='s'
while escolha=='s':
    altura=float(input('Digite sua altura: '))
    peso=float(input('Digite seu peso: '))
    imc=peso/(altura*altura)
    if imc>18.5:
        print('Você está abaixo do peso. ')
    elif imc<18.5 and imc>25:
        print('Você possui o peso ideal!\nContinue assim!')
    elif imc>25 and imc<30:
        print('Você está com sobrepeso!\nCuide sua alimentação!!!')
    elif imc>30 and imc<40:
        print('Você atingiu a obesidade!\nConsulte um especialista!!!')
    elif imc>40:
        print('Atenção, você está com obesidade morbida!\nConsulte urgentemente um especialista')
    else:
        print('!!! ERRO !!!\n OPÇÃO INVALIDA.')
    escolha=str(input('DESEJA REPETIR A OPERAÇÃO?\n[S/N] ')).lower()