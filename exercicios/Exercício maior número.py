n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n2 > n1:
    print('Numero maior: {}'.format(n2))
elif n1 > n2:
    print('Numero maior: {}'.format(n1))
else: print('Os numeros são iguais')
