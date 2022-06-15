import random
n1=str(input('Digite o nome do primeiro aluno: '))
n2=str(input('Digite o nome do segundo aluno: '))
n3=str(input('Digite o nome do terceiro aluno: '))
n4=str(input('Digite nome do quarto aluno: '))
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print(f'Dentre os alunos: {n1}, {n2}, {n3}, {n4}, o professor escolheu: {escolhido} para apagar o quadro!')
