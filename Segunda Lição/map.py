#Modo hard de criar lista, poxas

x = [i for i in range(12, 26)]
#print(x)

#Tudo antes do 18 vira 10 kkks
x = list (map(lambda x: 10 if x < 18 else(x), x))
print(x)


#Filtrando com lambda
x = list (filter(lambda x: x < 18, x))
print(x)

#Com map podemos fazer todos valores virarem 10
#Mapeamento
x = list (map(lambda x: 10, x))
print(x)


