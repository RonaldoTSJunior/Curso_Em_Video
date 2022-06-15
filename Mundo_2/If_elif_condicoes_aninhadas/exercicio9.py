# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento.
# à vista - dinheiro/cheque = 10% desconto
# à vista no cartão - 5% desconto
# em até 2x no cartão - preço normal
# 3x ou mais - 20% juros 
print('''---------FECHAMENTO DA VENDA---------
* POR FAVOR INFORME O VALOR DE SEU PRODUTO E ESCOLHA SUA FORMA DE PAGAMENTO *
[1] Dinheiro/cheque (10% Desconto)
[2] Débito ou crédito 1x (5%)
[3] 2x Cartão de crédito (Sem Desconto)
[4] 3x Cartão de crédito (20% juros)
''')
novamente='s'
while novamente=='s':
    usuario=float(input('Digite o valor de seu produto: R$ '))
    pagamento=int(input('Escolha sua forma de pagamento: '))
    if pagamento==1:
        print(f'Você escolheu Dinheiro/Cheque.\nValor final R$ {usuario-(usuario*0.1):.2f}')
    elif pagamento==2:
        print(f'Você escolheu Débito ou Credito 1x.\nValor final R$ {usuario-(usuario*0.05):.2f}')
    elif pagamento==3:
        print(f'Você escolheu Cartão de crédito em 2x.\nValor final R$ {usuario:.2f}')
    elif pagamento==4:
        print(f'Você escolheu Cartão de crédito em 3x.\nValor final R$ {(usuario*0.2)+usuario:.2f}')
    else:
        print('!!!ERROR!!!\nVALOR NÃO ENCONTRADO NO SISTEMA. ')
    novamente=str(input('DESEJA REFAZER A OPERAÇÃO?\n[S/N]  ')).lower()