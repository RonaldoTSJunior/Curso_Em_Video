# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.
print('''
         INSTRUÇÕES
     Genêros: M ou F    
''')

sexo='M','F'
novamente='S'
while novamente =='S':
    nome=str(input('Digite seu primeiro nome: ')).capitalize().strip()
    sexo=str(input('Digite seu genêro: ')).upper().strip()
    if sexo=='M':
        print(f'Olá {nome}, você é do genêro masculino!')
        novamente=str(input('Deseja continuar? [S/N]: ')).upper().strip()
    elif sexo=='F':
        print(f'Olá {nome}, você é do genêro feminino!')
        novamente=str(input('Deseja continuar? [S/N]: ')).upper().strip()
    else:
        print('Opção inválida, tente novamente...')
print(f'Acabou!')


