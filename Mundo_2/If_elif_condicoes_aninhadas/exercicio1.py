# Escreva um programa para aprovar o emprestimo bancario de uma casa.
# O programa vai perguntar "O VALOR DA CASA", "O SALÁRIO DO COMPRADOR", e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou entao ela será negada.
print('------\33[1;31;47mBANCO SANTO ANDRÉ\33[m------')
print('.\n.\n.\nCARREGANDO SISTEMA, POR FAVOR AGUARDE!\nBem Vindo!\nVamos começar sua cotação\n.\n.\n.\n')
comprador = str(input('Qual o seu nome? ')).capitalize()
valor_casa = float(input('Digite o valor do imóvel que deseja comprar: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
meses = anos*12
mensalidade = valor_casa/meses
limite = salario*0.3
if mensalidade > limite:
    print('Compra negada')
else:
    print(f'Sua cotação está pronta {comprador}!\nO valor a ser pago mensalmente será de R${mensalidade:.2f}!\nLevará {meses} para concluir o pagamento.\nO Banco Santo André agradece sua preferência!\nTenha um ótimo dia!\n')