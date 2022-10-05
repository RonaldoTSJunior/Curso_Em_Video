# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SOLUÇÃO MINHA

# principal=[]
# lista=[]
# calculo=0
# while True:
#     nome=str(input('Digite o nome do aluno: ')).capitalize().strip()
#     nota1=float(input('Digite a primeira nota: '))
#     nota2=float(input('Digite a segunda nota: '))
#     lista.append(nome)
#     lista.append(nota1)
#     lista.append(nota2)
#     principal.append(lista[:])
#     lista.clear()
#     escolha=str(input('Deseja adicionar mais alunos? [S/N]: ')).strip()
#     if escolha in 'Nn':
#         break
# print('-=' * 5, 'BOLETIM', '=-' * 5)
# print(f'{"Nº":<4}{"NOME ":^10}{"NOTA":>8}')
# print('-' * 25)
# for numerado,lista in enumerate(principal):
#     print(f'{numerado:<4}{lista[0]:^10}{(lista[1]+lista[2])/2:>8}')
# print('-'*25)
# while True:
#     individual=int(input('Digite o código do aluno para suas notas individualmente (999 para encerrar o programa.): '))
#     if individual == 999:
#         print('Finalizando...\n<<<VOLTE SEMPRE!>>>')
#         break
#     elif individual >= 0 and individual < 999:
#         print(f'{principal[individual][0]} - [{principal[individual][1]} - {principal[individual][2]}]')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SOLUÇÃO CURSO EM VIDEO 

aluno=[]
while True:
    nome=str(input('Digite o nome do aluno: ')).capitalize().strip()
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    media=(nota1+nota2)/2
    aluno.append([nome,[nota1,nota2],media])                                  #Deste modo posso criar uma lista composta já pronta com todos os elementos dentro!
    escolha=str(input('Deseja adicionar mais alunos? [S/N]: ')).strip()
    if escolha in 'Nn':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for posicao, ficha in enumerate(aluno):
    print(f'{posicao:<4}{ficha[0]:<10}{ficha[2]:>8.1f}')                       #Comandos para definir espaçamentos. EX:<10 para 10 espaços a esquerda.
while True:
    individual=int(input('Digite o código do aluno ou 999 para encerrar: '))
    if individual >= 0 and individual < 999 and individual < len(aluno):
        print('-'*30)
        print(f'{aluno[individual][0]} - {aluno[individual][1]}')              #Utilizando este metodo consigo inserir dentro da lista composta 'Aluno', o código do aluno que no caso se refere a posição do mesmo na lista aluno, e mostrando qual item na posição tal dentro desta lista usando [1] eu mostro que quero que o programa me devolva a primeira e segunda nota!
    elif individual >= len(aluno):
        print('-'*30)
        print('Aluno não cadastrado! TENTE NOVAMENTE')
    elif individual == 999:
        print('-'*30)
        print('Finalizando...\n<<<VOLTE SEMPRE!>>>')
        break