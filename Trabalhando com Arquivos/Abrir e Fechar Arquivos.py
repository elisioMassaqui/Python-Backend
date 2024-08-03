#Criar arquivo modo tradicional
file = open('exemplo.txt', 'w')
file = file.write('Escrevendo file no file')
#Abrir pra leitura arquivo modo tradicional
file = open('exemplo.txt', 'r')

#Ler arquivo modo tradicional
conteudo = file.read()
print(conteudo)
#Fechar arquivo modo tradicional
file.close

#Você também pode usar o gerenciador
#De contexto with, que fecha o arquivo automaticamente:
with open('exemplo.txt', 'r') as arquivo:
    content = arquivo.read()
    print('With Open:', content)