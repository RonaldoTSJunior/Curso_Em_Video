#MODULOS:
#-> Fragmentar projetos maiores em pequenos módulos para facilitar a legibilidade e entendimento, tornando assim a manutenção muito mais tranquila.


#PACOTES:
# -> Um pacote nada mais é, que uma pasta que contém módulos ou como já conhecemos e trabalhamos com: BIBLIOTECAS.

#Ex: o Arquivo UTEIS conter diversas funções, eu posso separar essas funções por assuntos: números, strings, datas, cores. Cada assunto contendo suas respectivas funções.

#Tornando assim a importação muito mais prática e fácil, por exemplo: import números irá importar todas as funções dentro do assunto números.


#Aula prática:

#import uteis    #Transferindo as def's para outro arquivo, e importando o arquivo contendo as funções que serão utilizadas do módulo uteis.

#from uteis import fatorial,dobro,triplo    #Importando apenas as funções que serão utilizadas.

#Sempre cuidar se já existe alguma função presente no programa, para não ocorrer incompatibilidades com funções já existentes. 

#Ex: a função já existir, e eu importar outra função chama dobro.

#Para evitar esse conflito, basta importar o modulo inteiro e quando chamar a função utilizar "nome_do_modulo.função()".
from uteis import numeros

#Programa principal:
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O Fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")