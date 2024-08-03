def lista_quadrados(lista):
    quadrados = []
    for num in lista:
        quadrados.append(num ** 2)
    return quadrados
    
print(lista_quadrados([1, 2, 3, 4, 5]))