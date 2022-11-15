# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Não está acessível no momento')
else:
    print('Está acessível no momento!')