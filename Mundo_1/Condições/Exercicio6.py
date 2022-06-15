p=int(input('Primeiro número: '))
s=int(input('Segundo número: '))
t=int(input('Terceiro número: '))
maior=p
if (s>maior):
    maior=s
if (t>maior):
    maior=t
print(f'O maior número é: {maior}')
menor=p
if (s<menor):
    menor=s
if (t<menor):
    menor=t
print(f'O menor número é: {menor}')