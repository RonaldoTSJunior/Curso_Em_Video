#crie uma tupla que contenha até o numero 20 por extenso, e peça ao usuario um numero, dando a ele esse numero por extenso
extenso=('Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
print('Digite números entre 1 e 20 para obter seu nome por extenso.\nLembrando! O número * 0 * finaliza o programa.')
while True:
    usuario=int(input('Digite um número entre 1 e 20: '))
    escolha=str(input('Deseja Prosseguir? [S/N]: ')).upper().strip()
    if escolha=='S':
        if usuario==0:
            print('Você digitou Zero.\nFinalizando\n.\n.\n.')
            break
        elif usuario==1:
            print(f'Voce digitou o número *',extenso[0],'*')
        elif usuario==2:
            print(f'Você digitou o número *',extenso[1],'*')     
        elif usuario==3:
            print(f'Você digitou o número *',extenso[2],'*')
        elif usuario==4:
            print(f'Você digitou o número *',extenso[3],'*')
        elif usuario==5:
            print(f'Você digitou o número *',extenso[4],'*')
        elif usuario==6:
            print(f'Você digitou o número *',extenso[5],'*')
        elif usuario==7:
            print(f'Você digitou o número *',extenso[6],'*')
        elif usuario==8:
            print(f'Você digitou o número *',extenso[7],'*')
        elif usuario==9:
            print(f'Você digitou o número *',extenso[8],'*')
        elif usuario==10:
            print(f'Você digitou o número *',extenso[9],'*')
        elif usuario==11:
            print(f'Você digitou o número *',extenso[10],'*')
        elif usuario==12:
            print(f'Você digitou o número *',extenso[11],'*')
        elif usuario==13:
            print(f'Você digitou o número *',extenso[12],'*')
        elif usuario==14:
            print(f'Você digitou o número *',extenso[13],'*')
        elif usuario==15:
            print(f'Você digitou o número *',extenso[14],'*')
        elif usuario==16:
            print(f'Você digitou o número *',extenso[15],'*')
        elif usuario==17:
            print(f'Você digitou o número *',extenso[16],'*')
        elif usuario==18:
            print(f'Você digitou o número *',extenso[17],'*')
        elif usuario==19:
            print(f'Você digitou o número *',extenso[18],'*')
        elif usuario==20:
            print(f'Você digitou o número *',extenso[19],'*')
        else:
            print('Valor inválido! Tente novamente...')
            break
    else:
        print('Tudo bem então! Vamos finalizar...')
        break
print('Finalizado... Até a proxima!')