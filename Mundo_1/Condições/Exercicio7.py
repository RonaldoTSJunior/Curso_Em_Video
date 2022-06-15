salario=float(input('Digite o seu salário para o calculo de aumento: '))
print('O salário base é de R$1250.00, acima a este valor receberá um aumento de 10%, abaixo ou igual a este valor receberá um aumento de 15%.')
if (salario>1250):
    print(f'Seu aumento será de 10%, e ficará R${salario*0.10+salario:.2f}. ')
else:
    (salario<1250), print(f'Seu aumento será de 15%, e ficará R${salario*0.15+salario:.2f}')
