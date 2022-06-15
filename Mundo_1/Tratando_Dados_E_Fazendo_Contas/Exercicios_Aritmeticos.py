n1=int(input('Digite um valor '))
n2=int(input('Digite outro valor '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {} o produto é {} e a divisão é {:.3f}'.format(s,m,d),end=' ======= ')       
print('A divisão inteira é {} e a potência é {}'.format(di,e))









#End=' ' serve para juntar os dois prints na mesmo linha. 
#Utilizando a str dentro de (End='') pode-se separar os dois prints com sinais ou caracteres mesmo estando no mesma linha
#O \n serve para quebrar a linha onde desejar.
#A formatação :.3f serve para limitar em 3 casas decimais do resultado após o. (Não se limitando a 3)