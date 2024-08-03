def contagem_elementos(lista):
    contagem = {}
    for elem in lista:
        if elem in contagem:
            contagem[elem] += 1
        else:
            contagem[elem] = 1
    return contagem
print(contagem_elementos([1, 2, 3, 4, 5, 6]))
    