#Aqui dentro do with ele cria um gerenciador de contexto
#Fazendo com que abra e fecha o arquivo automaticamente

with open('pessoal.text', 'r') as arq:
    x = arq.read()
    print("Lidooo:", x)