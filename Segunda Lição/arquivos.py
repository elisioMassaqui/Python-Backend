#Letras de arquivo editor open
# "r" leitura
# "w" escrita subscrever
# "a" escrita adicionando

#Pra ler o que está num arquivo, letra deve ser "r"
#Mas se for "w" deve ser pra escrita
arquivos = open('persona.txt', 'r')
resultados = arquivos.readlines()

#Cada linha se torna uma posição
x = []

#Iterar entre os arquivos e guardar
#Tudo em x na forma splitado
for i in resultados:
    x.append(i.split())
print(x)
#Matrizes e listas e dicionarios são mesmo interessantes
print(x[0], x[1], x[2], x[3])
print(x[1], x[2], x[3])
print(x[2], x[3])
print(x[3])
print(resultados)

x = []
y = 0
while True:
    if y > 3:
        break
    #Com w de write ele subscreve e com a apenas append
    with open('gerente.cpp', 'a', encoding='UTF-8') as gerente:
        gerente.write(input('Digite alguma coisa: ') + '\n')
    
    with open('gerente.cpp', 'r') as lerCode:
        leitura = lerCode.readlines()

    y += 1
print(leitura)

#Só que essa não é a forma mais apropriada de trabalhar
#A não ser que queiras correr o risco de deixar o arquivo aberto
#Pra criar arquivo e escrever algo 
arquivo = open('pessoas.txt', 'w')
x = open('pessoas.txt', 'r')

i = 0
while True:
    if i > 1:
        break

    #Essa é a prova que virgula é diferente de concatenar
    arquivo.write(input('Digite o seu nome:') + '\n')
    i += 1
arquivo.close()

print(x.read())
x.close()
