# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#================================EXERCICIO COM LISTA===================================
print('='*100)
print(" "*25,"BEM VINDO AO VERIFICADOR DE EXPRESSÕES!!")
expressao=input('Digite sua expressão: ').strip()
parenteses=[]
for simbolo in expressao:
    if simbolo in '(':
        parenteses.append('(')
    elif simbolo in ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses)==0:
    print('EXPRESSÃO VÁLIDA! TODOS OS PARENTESES ESTÃO FECHADOS!')
elif len(parenteses)!=0:
    print('EXPRESSÃO INVÁLIDA! VERIFIQUE OS PARENTESES E TENTE NOVAMENTE.')
#================================EXERCICIO SEM LISTA====================================
# expressao=input('Digite sua expressão: ').strip() 
# parenteses_esquerda=0
# parenteses_direita=0
# for parenteses in expressao:
#     if parenteses in '(':
#         parenteses_esquerda+=1
#     if parenteses in ')':
#         parenteses_direita+=1
# if parenteses_direita != parenteses_esquerda:
#     print('EXPRESSÃO INCORRETA! PARENTESES ABERTOS NA EXPRESSÃO, REVISE A EXPRESSÃO!')
# elif parenteses_direita == parenteses_esquerda:
#     print('EXPRESSÃO CORRETA! SEUS PARENTESES ESTÃO TODOS FECHADOS.')
