#ANSI ESPACE SEQUENCE
#Código para adicionar cores ao terminal. Ex: \033[style;text;backgroundm
#códigos de cores para style que funcionam melhor no terminal: 0(significa sem style),1(Negrito),4(sublinhado) e 7(negativo, irá inverter a ordem das cores para letra e fundo) 
#Códigos de cores para text vão de: 30 a 37. sendo 37(branco)31(vermelho)32(verde)33(amarelo)34(azul)35(roxo)36(azul claro)30(cinza)
#Códigos de cores para background vão de: 40 a 47, seguindo o mesmo padrão das cores de texto.
#EXEMPLO PRÁTICO:
#print('\33[1;31;40mOlá Mundo')   #adicionar um \33[m ao final da string fara com que a coloração do background fique apenas na frase

#Utilizando dentro de um print com formatação
#a=3
#b=5
#print(f'Os valores são \33[1;35;40m{a} e \33[4;36;47m{b}\33[m')
#CRIANDO CORES
#nome='Ronaldo'
#Cores={'limpa':'\033[m','azul':'\033[34m','pretoebranco':'\033[7;37m','amarelo':'\033[33m'}
#print(f"Olá, Muito prazer em te conhecer, {Cores['pretoebranco']}{nome}{Cores['limpa']} ")
