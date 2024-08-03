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