# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
# desenvolvida no desafio 108.
from monetario import moeda

#Programa principal:

user = float(input('Digite um valor: '))
print(f'O valor {moeda.moeda(user)} aumentado 10% fica {moeda.aumentar(user, False)}')
print(f'O valor {moeda.moeda(user)} diminuído em 15% fica {moeda.diminuir(user, False)}')
print(f'O valor {moeda.moeda(user)} dobrado fica {moeda.dobro(user, False)}')
print(f'O valor {moeda.moeda(user)} pela metade fica {moeda.metade(user, False)}')