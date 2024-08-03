
#Retornar
def soma(*args, x=10):
    
    #Se for maior, sai sem fazer nada
    if x >= 10:
        return 380
    
    print(sum(args))

#Se for igual a 10
somado = 'Se valor for 10:', "Return ao invés da operação com args ou none se não:", soma( 3, 5, 8, 9)
print(somado)

#Se for igual 10, retorna o valor do retorno
#O valor do retorno pode ser operação ou var
#Recebemos o valor do retorno
print('Printado porque é igual a 10 ou None se for diferente:', soma())

#Não recebemos o valor do retorno
print('Não recebemos o valor do retorno:', soma)

#Retorna 0 ou nada kkk, dá no mesmo
soma()


