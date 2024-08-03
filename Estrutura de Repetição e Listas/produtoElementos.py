def produto_elementos(lista):
    produto = 1
    arrary = []
    global num
    num = []
    #Ele itera sob todos valores da lista
    #se tornando a própria lista
    #e os seus valores podem ser usado numa operação
    for num in lista:
        print(type(num))
        print(type(arrary))
        produto *= num
    return produto
print(produto_elementos([1, 2, 3, 4, 5]))