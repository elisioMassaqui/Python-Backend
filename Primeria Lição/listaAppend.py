nomes = ['marcus']

print(nomes)
#Adicionar tipos de dados na lista dinamicamente
nomes.append('joana')
nomes.append('emilia')

print(len(nomes))
print(nomes)

nomes.append(not False)
nomes.append( not True)

tamanho = len(nomes)
for i in range(0, tamanho):
    print(nomes[i])

#Adicionados a lista e imprimidos, news datassss
idades = []

while True:
    print('Digite a sua idade ou -1 pra sair')
    idade = int(input())

    if idade == -1:
        break

#Somente numeros divisor de 2
    if idade % 2 == 0:
        idades.append(idade)

print(idades)