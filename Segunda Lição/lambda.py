def minhaFunc():
    print('ola')
minhaFunc()

#Função lambda, sintaxe mais curta, sempre retorna algo
#Não precisa necessariamente ser declarada

#O interpretador python percebe que é uma função lambda
#E atribui a classe function do tipo lambda
x = lambda: print('hello')
print(x)
print(x())
x()

#Retorno
x = lambda: 10
print(x)
print(x())
x()

#Paramentros
x = lambda nome, idade: print(f'nome = {nome}\nidade = {idade}')
x('elisio', 21)

#Com argumentos limitados, impacotados em uma tupla
x = lambda *args: print(args)
x('elisio', 'massaqui', 'luamba', 21, not False)

#Definição que retorna função lambda com ou sem args
def teste():
    return lambda *args: print(args)
y = teste()
y('caio', 'marcus', 'prof', 'brazuca')
