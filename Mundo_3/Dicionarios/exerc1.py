#Faça um programa que leia nome e média de um aluno, guardando também a situação (Aprovado, reprovado, recuperação) em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
perfil=dict()
perfil['Aluno'] = str(input('Nome do aluno: '))
perfil['Media'] = float(input('Media do aluno: '))
if perfil['Media'] >= 7:
    perfil['Situação'] = 'Aprovado.'
elif perfil['Media'] >= 5 and perfil['Media'] < 7:
    perfil['Situação'] = 'Recuperação.'
elif perfil['Media'] < 5:
    perfil['Situação'] = 'Reprovado.'
print('-='*35)
#print(f'Aluno = {perfil["Aluno"]}.\nMedia = {perfil["Media"]}.\nEle foi/está {perfil["Situação"]}')
for key,value in perfil.items():
    print(f'{key} - {value}')
print('-='*35)