      #FATIAMENTO DE STRING
#frase='Curso em video python'    #frase='Curso em video Python'
#print(frase[9::3]) (Fatiar a partir do 9° char até o final, de 3 em 3)              #print(frase[9])  (Fatiar somente o 9° char da str)
      #ANALISE DE STRING
#frase='Curso em video python'
#print(len(frase))   (Comprimento da frase)
#frase='Curso em video python'
#print(frase.count('o'))   (Serve para contar quantas x a letra especificada aparece na string)
#frase='Curso em video python'
#print(frase.find('deo'))  (Serve para mostrar em qual número começou a frase )
#frase='Curso em video python'
#'Curso' in frase    (O operador IN irá verificar se a palavra 'Curso' existe dentro da variavel e me retornara com true ou false)
       #TRANSFORMAÇÃO DE STRING
#frase='Curso em video python'
#print(frase.replace('python','Android'))       (Substitui a palavra indicada(python) pela palavra escolhida(Android) )
#frase='Curso em video python'
#print(frase.lower())             (Transforma a string da variavel em maiusculo'upper', ou minusculo'lower')
#frase='Curso em video python'
#print(frase.capitalize())         (Transforma todas as letras em minusculas e deixa apenas a primeira letra maiuscula)
#frase='Curso em video python'
#print(frase.title())               (Transforma a string em um titulo, colocando todas as palavras com letras iniciais maiusculas)
#frase='   Aprenda Python   '
#print(frase.strip())                (Remove os espaços não utilizados que o usuario colocou na caixa de texto)
#frase='   Aprenda python   '
#print(frase.rstrip()) irá remover os espaços inuteis extras a direita da frase e print(frase.lstrip()) irá remover os espaços inuteis extras a direita
       #DIVISÃO DE STRING
#frase='Curso em video python'
#print(frase.split())       (Separa as palavras que possuem um espaço entre elas em novas strings '', e as coloca dentro de listas)
       #JUNÇÃO DE STRING
#frase='Curso em video python'
#print('-'.join(frase))          (Vai juntar as palavras separadas por espaços em uma string por algum elemento pré definido)


 











#len()  (Ánalisar o comprimento da str).
#variável.count('')  (Contar quantas x a letra especificada aparece na string), variavel.count('o',0,13)  (Serve para contar quantas x a letra especificada aparece na str já com o fatiamento).
#Lembrando que na contagem ex:(9:13) o ultimo valor sempre é ignorado e contado o anterior.
#find()  (Mostra em qual número começou a frase especificada)   (Receber valor negativo como resposta da busca, significa que a frase não existe na string).
#''in variavel (Irá me retornar com true ou false se a frase indicada existir dentro da variavel)