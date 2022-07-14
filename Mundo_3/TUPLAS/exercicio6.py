# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras=("TRABALHO","LOJA","CURSO","GRUPOS","ACADEMIA","CIDADES","MERCADO","PROGRAMADOR","LOJISTA","TRABALHADOR","CELULAR")
vogais=("A","E","I","O","U")
for palavra in range(len(palavras)):
    print(f'\nNa palavra {palavras[palavra]} temos as vogais: ',end='')
    for vogal in range(len(vogais)):
        if vogais[vogal] in palavras[palavra]:
            contagem=palavras[palavra].count(vogais[vogal])
            print(f'{vogais[vogal]}'*contagem,end=' ')