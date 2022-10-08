# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.
def lin(txt):
    print('-'*40)
    print(txt)
    print('-'*40)
    
    
def area(l,c):
    metro_quadrado = l * c
    print(f'- LARGURA: {area1}m.\n- COMPRIMENTO: {area2}m.\n- ÀREA: {metro_quadrado}m²')


#Programa principal:
lin('Controle De Terreno')
area1=(float(input('Digite o valor da Largura (m): ')))
area2=(float(input('Digite o valor do Comprimento (m): ')))
area(area1,area2)
