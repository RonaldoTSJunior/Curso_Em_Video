import moeda
import dado

#Programa principal:
user = dado.leiadinheiro('Digite o valor que deseja analisar: R$')  # type: ignore
moeda.resumo(user, 35, 12)  # type: ignore
