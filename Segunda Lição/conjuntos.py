#Não permite merdas repetidas

x = [1,1,1,2,2,3,4,5]

#converter pra um set, conjunto
x = set(x)
print(x)

#Unir um conjunto ao outro evitando valores já existentes

y = {1, 2, 3, 4, 5, 10, 7}
z = {6, 7, 8, 9, 10, 5, 2, 1, 11, 20}

c = y.union(z)
print(c)

#Interceçção, mosrtar valores apenas interceptados
# De de dois conjuntos, valores iguais ou seja repetidados um pro outro

c = y.intersection(y)
print(c)

#Mostrar valores diferentes de um conjunto pra com outro

c = z.difference(y)
print(c)
