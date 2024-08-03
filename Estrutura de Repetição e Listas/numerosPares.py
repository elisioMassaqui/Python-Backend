def posicoes_pares(list):
    posicoes = []
    for i, num in enumerate(list):
        if num % 2 == 0:
            posicoes.append(i)
    return posicoes
print(posicoes_pares([1, 2, 3, 4, 5, 6]))