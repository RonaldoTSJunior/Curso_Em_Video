# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*n, sit=False):
    '''
    => Função para análise de notas da turma.
    :param n: Recebe as notas da turma (aceita várias).
    :param sit: Mostra a situação da turma de acordo com a média: Acima  ou igual a 7 aprovado, 6 ou 5 recuperação, e abaixo de 5 reprovado.
    :return: Dicionário contendo as informações da turma.
    '''
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = (sum(n)) / len(n)
    if sit:
        if turma['media'] >= 7:
            turma['situacao'] = str('EXCELENTE')
        elif turma['media'] < 7 and turma['media'] >=5:
            turma['situacao'] = str('RECUPERAÇÃO')
        else:
            turma['situacao'] = str('REPROVADOS')
    return turma
    
#Programa Principal
resp = notas(1.5,5.5,4,10, sit=True)
help(notas)
