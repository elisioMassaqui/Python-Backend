#REMOVER PELOS VALORES E NÃO INDICE
# QUANDO NÃO SABE OS EM QUE POSIÇÃO ESTÁ O VALOR 
# MAS PRECISAMOS REMOVER

idades =[10, 20, 30, 40, 20, 50, 30]

#Mas não retorna o valor removido, coisa que o pop fazia 
# Aqui retorna NONE
print(idades.remove(50))
print(idades)

#Remove apenas o primeiro dos gemeos
idades.remove(20)
idades.remove(30)
print(idades)



