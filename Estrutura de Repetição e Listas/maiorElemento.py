def maior_elemento(lista):
    maior = lista[5]
    for num in lista:
        if num > maior:
            maior = num
    return maior

print(maior_elemento([1, 3, 5, 12, 9, 0]))