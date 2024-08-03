#Excluir valor de uma lista pelo index
#O python já faz a realocação dos valores automaticamente fazendo atual se mover pra próxima

idades = [10, 20, 30, 40, 50]
#Excluiu o ultimo e retornou o mesmo
print(idades.pop())
print(idades)

#Removemos um valor pelo indice nesse caso 1
valorRemovido = idades.pop(1)
print(valorRemovido)
print(idades)
