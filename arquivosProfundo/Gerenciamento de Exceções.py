try:
    with open('arq.txt', 'r') as file:
        conteudo = file.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except PermissionError:
    print("Permissão negada para acessar o arquivo.")
