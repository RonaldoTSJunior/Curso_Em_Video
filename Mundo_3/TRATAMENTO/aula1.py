#TRATAMENTOS DE ERROS:
#Dentro do python seguidamente nos depararemos com diversos erros, e cada erro possuí sua própria característica como erro de type, syntax, value, etc...
#Com a CLASSE Exception (lê-se EXCEÇÃO) podemos contornar estes erros utilizando (try: e except:), que nos permite listar os possíveis erros que ocorrerão e adicionar o tipo de erro (exceção) que será devolvido.
#Exemplo
try:                                                #Com este comando ele irá tentar o bloco dentro dele.
    a = int(input('Númerador: '))      
    b = int(input('Denominador: '))
    r = a / b

#Conforme os "except" abaixo, podemos especifícar o que iremos mostrar ao usuário se acontecer os erros determinados.
#except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')
    
# #except ZeroDivisionError:
#     print('Não é possível efetuar divisões por zero!')   
    
# #except KeyboardInterrupt:
#     print('\nO usuário preferiu não informar os dados.')
    
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}, e a causa deste erro foi {erro.__class__}')
#except Exception as erro:                                             #Caso dê erro, o except irá devolver uma mensagem de erro.
    #print(f'O Problema encontrado foi {erro.__class__}')              #Podemos personalizar a mensagem de erro com a classe Exception,
    
else:
    print(f'O resultado foi {r:.1f}')               #Caso funcione tudo normalmente como deveria, o else irá devolver o resultado do programa.

finally:
    print('Volte sempre!!')                         #Este comando é executado independente de erro ou acerto no programa, e será executado sempre ao final do mesmo.