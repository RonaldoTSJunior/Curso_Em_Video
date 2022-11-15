# Crie um módulo chamado moeda.py que tenha as funções incorporadas: 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from monetario import moeda

#Programa principal:

user = float(input('Digite um valor: '))
print(f'O valor {user} aumentado 10% fica {moeda.aumentar(user)}')
print(f'O valor {user} diminuído em 15% fica {moeda.diminuir(user)}')
print(f'O valor {user} dobrado fica {moeda.dobro(user)}')
print(f'O valor {user} pela metade fica {moeda.metade(user)}')
