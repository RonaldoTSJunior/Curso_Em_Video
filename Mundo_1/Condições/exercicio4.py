d=float(input('Quantos quilometros sua viagem terá? '))
if d<=200:
    print(f'A sua viagem possui 200km ou menos, a passagem custará R${(0.50*d):.2f}')
elif d>200:
    print(f'A sua viagem possui mais de 200km, a passagem custará R${(0.45*d):.2f}')