def filtro(lista, alvo):
    filtrados = []
    for num in lista:
        if num > alvo:
            filtrados.append(num)
    return filtrados
print(filtro([1, 2, 3, 4, 5], 0))