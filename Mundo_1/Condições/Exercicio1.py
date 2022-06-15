import random
n1=random.randint(0,5)
n2=int(input('Qual número você acha que é? '))
if n2 == n1:
    print('Parabéns, você acertou!')
else:
    print('infelizmente você errou!')
print(f'O resultado foi: {n1}')
