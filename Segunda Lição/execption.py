#Cada excessão pra problema diferente

#Aqui temos excessões com
#Respostas personalizadas
try:
    x = int(input())
    print(5 / x)
except ValueError:
    print('Digite um numero inteiro, por favor')
except ZeroDivisionError:
    print('Digite algo diferente de 0')

#Pra todos tipos de excessões, só que
#Não dá pra personalizar a resposta
#Mas perfeito pra testes
try:
    y = int(input())
    print(10 / y)
except Exception as erro:
    print(f'Sua excessão foi "{erro}", tente reparar no try')