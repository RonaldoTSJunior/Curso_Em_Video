# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from monetario import moeda

#Programa principal:

user = float(input('Digite um valor: '))
moeda.resumo(user, 80, 26)