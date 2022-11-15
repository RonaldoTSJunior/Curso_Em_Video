# Adapte o código do desafio #107
# Criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from monetario import moeda

#Programa principal:

user = float(input('Digite um valor: '))
print(f'O valor {moeda.moeda(user)} aumentado 10% fica {moeda.moeda(moeda.aumentar(user))}')
print(f'O valor {moeda.moeda(user)} diminuído em 15% fica {moeda.moeda(moeda.diminuir(user))}')
print(f'O valor {moeda.moeda(user)} dobrado fica {moeda.moeda(moeda.dobro(user))}')
print(f'O valor {moeda.moeda(user)} pela metade fica {moeda.moeda(moeda.metade(user))}')