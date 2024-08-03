#Leitura Linha por Linha
with open('arquivo.txt', 'r', encoding='UTF8') as file:
    for linha in file:
        print("Ler linha por linha o arquivo: ", linha.strip())

#Leitura e Escrita Binária
with open('arquivo.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')
    print("Escrita binária: ", file)

with open('arquivo.bin', 'rb') as file:
    conteudo = file.read()
    print("Leitura binária: ", conteudo)