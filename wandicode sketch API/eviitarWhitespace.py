x = 10
criar = 'w'
escrever = 'a'
ler = 'r'
ficheiro = 'arquivo.txt'

#Strip pra evitar whitespaces
nomeArquivo = input('Digite nome do arquivo: ').strip()

with open(ficheiro, escrever) as file:
    arquivo = file.write((nomeArquivo) + '\n')

with open(ficheiro, ler) as file:
   print(file.read())