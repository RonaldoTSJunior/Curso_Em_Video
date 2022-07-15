# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista_numeros=[]
for sequencia in range(5):
    user=int(input('Digite um valor: '))
    if sequencia == 0 or user > lista_numeros[len(lista_numeros)-1]:    # Verifica se ele é o primeiro valor ou se ele é maior que o ultimo valor na lista
        lista_numeros.append(user)
        print('Valor adicionado ao final da lista!')
    else:
        posicao=0                                    # Variavel posicao para descobrir a posicao em que se encontra o valor caso ele não seja pertença a verificação do IF
        while posicao < len(lista_numeros):          # Enquanto a var posicao for menor que o tamanho da lista executará o bloco abaixo
            if user <= lista_numeros[posicao]:       # Se o input for menor ou igual a posicao na lista, é usado o insert para adicionar o user na posicao da variavel posicao.
                lista_numeros.insert(posicao, user)
                print(f'Valor adicionado na posição {posicao}')
                break                                # Break para sair do laço ao finalizar o processo.
            posicao+=1                               # Para avançar as posições
print('-='*35)
print(f'Os valores digitados na ordem foram:',lista_numeros)