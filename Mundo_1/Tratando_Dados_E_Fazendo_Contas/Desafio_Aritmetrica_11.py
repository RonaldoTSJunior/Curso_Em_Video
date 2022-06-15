d=int(input('Você alugou este carro por quantos dias? '))
q=float(input('Por quantos quilômetros você percorreu com este carro? '))
print(f'Aluguei este carro por {d} dias, e andei {q} Km com este carro.')
print(f'Certo, o valor a pagar ficou por R${(d*60)+(q*0.15):.2f}.')