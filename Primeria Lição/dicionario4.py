# Endereço de memoriaaaa

x= {'Nome': 'Elisio'}

# Aqui a variavel z não é igual aos valores de x e sim igual
# Ao endereço de memoria de x que vai nos trazer os valores

z = x
print('Copiamos apenas os endereços de memória ou seja as chaves\n', z)


# Já aqui a variavel z copiou ou seja acessou apenas os valores
# Diretamente do dicionario e alterou
z = x.copy()
z['Nome'] = 'Marcus'
print('Copiamos os valores das chaves\n', z)