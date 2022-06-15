import math
n1=int(input('Digite seu número: '))
raiz= math.sqrt(n1)
print(f'A raiz quadrada de {n1} é igual a {math.ceil(raiz):.2f}')















#import math: importa a biblioteca ''math'' inteiro para a utilização dentro do código. 
#from math import (importa somente uma das funções:floor ou ceil ou sqrt ou alguma outra função dentro da biblioteca math).
#import: importar uma biblioteca
#Dentro da biblioteca math podem ser encontrados estas funções e outras >>>(ceil: arredonda pra mais, floor: arredonda para menos, sqrt: raiz quadrada.)
#from math import (ctrl+space mostra todas as funcionalidades do modulo math)
# -*- coding: utf-8 -*-: Altera o encoding que o computador lê o código.
#O comando pip install (nome do modulo)