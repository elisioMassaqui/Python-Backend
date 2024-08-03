nomes = ['caio', 'marcus', 'josé', 'Andreia']

#Estás a acessar o indice rapaz
#nome = nomes[1]
#print(nome)

#Eu preciso me aprofundar mais nisso
for i in range(0, 4):
    print(i,'index de', nomes[i])
    tamanho = len(nomes)
    print('Tamanho da lista:', tamanho)

print()


print('Exemplos com tamanho:\n')
#Nesse caso vai de 0 a tamanho, caso não saibas o tamanho da lista ou prevenir erros
for i in range(0, tamanho):
    print(i, nomes[i])