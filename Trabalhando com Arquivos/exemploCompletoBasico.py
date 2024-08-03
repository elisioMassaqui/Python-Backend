import os
from pathlib import Path

# Criar um novo diretório
diretorio = Path('exemplo_diretorio')
diretorio.mkdir(exist_ok=True)

# Criar e escrever em um novo arquivo
arquivo = diretorio / 'exemplo.txt'
with open(arquivo, 'w') as file:
    file.write('Olá, Mundo!')

# Ler o arquivo
with open(arquivo, 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Listar arquivos no diretório
print(os.listdir(diretorio))

# Remover o arquivo e o diretório
arquivo.unlink()
diretorio.rmdir()
