#Filtrar coisas numa lista
x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#Filtrou todos elemtos de x que era menor que 18, mandou dentro dex
#É aqui onde lambda entra porque podemos ter um
#Retorno e iteraçã numa unica linha
x = list (filter(lambda x: x < 18, x))
print(x)


#Comparação e filtro entre dicionarios
#Quero só pessoas que tem 20 anos ou menos
y = [{'nome': 'elisio','idade': 22},
     {'nome': 'caio', 'idade': 40}
    ]

y = list (filter(lambda y: y['idade'] < 40, y))
print(y)
