# Faça um programa que mostre a contagem regressiva para fogos de artificio, de 10 a 0 com uma pausa de 1 segundo entre eles
#Contém uso de bilbiotecas.
import emoji
import time
print('''
---------ANO NOVO!!!---------
    [CONTAGEM REGRESIVA...]
''')
for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print(emoji.emojize(':fireworks:'))