with open('arquivo.txt', 'w',  encoding='UTF-8') as file:
    conteudo = file.write('Olá arquivo')
    print('Escrita: ', conteudo)

with open('arquivo.txt', 'r', encoding='UTF-8') as file:
    conteudo = file.read()
    print('Leitura: ', conteudo)