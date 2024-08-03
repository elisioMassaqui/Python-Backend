def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def lista_fatoriais(lista):
    fatoriais = []
    for num in lista:
        fatoriais. append(fatorial(num))
    return fatoriais
print(lista_fatoriais([1, 2, 3, 4, 5]))