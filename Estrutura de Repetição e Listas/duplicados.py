def remover_duplicados(lista):
    unicos = []
    for elem in lista:
        print(elem)
        if elem not in unicos:
            print(elem)
            unicos.append(elem)
    return unicos
print(remover_duplicados([1, 3, 5, 5, 6, 1, 4, 4, 6, 3, 3, 8, 9, 8]))