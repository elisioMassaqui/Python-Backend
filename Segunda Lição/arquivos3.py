#Criação do arquivo
#arquivo = open('arquivo.txt', 'w', encoding='UTF-8')
#arquivo.write('olá')

#Edição do arquivo
#arquivo = open('arquivo.txt', 'a', encoding='UTF-8')
#arquivo.write('oieeee\n')

### Abra o arquivo e ainda não fecha
#Edição do arquivo
arquivo = open('arquivo.txt', 'a', encoding='UTF-8')


### Campo de operações com arquivo aberto

#Cada nome dentro de uma linha
i = 3 ###
while True:
    if i > 1:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + '\n')

    i += 1

#Digitar nome e idade numa linha
x = 0
while True:
    if x > 1:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + ' ' + input('Digite a idade:  ') + '\n')
    x += 1

### Primeiro fecha manualmente, após operação anterior
arquivo.close()

### Abrir novamente
#E agora abra novamente, possibilitando um fluxo de atualização
#Leitura de arquivo
lerArquivo = open('arquivo.txt', 'r')
resultados = lerArquivo.read()
print(resultados)

resultadosRLs = lerArquivo.readlines()
x = []
for i in resultadosRLs:
    x.append(i.split())
    print(x[0][1])

###Fechar como garantia, antes do app terminar
arquivo.close()