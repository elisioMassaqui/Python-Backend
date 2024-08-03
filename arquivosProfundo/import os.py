#Manipulação de Diretórios#
#Usando os e pathlib
#os: Ideal para compatibilidade com sistemas mais antigos e tarefas simples.
#pathlib: Mais moderno e orientado a objetos.

import os

# Caminho absoluto
caminho_absoluto = os.path.abspath('arquivo.txt')
print(caminho_absoluto)

# Verificar se é um arquivo ou diretório
print(os.path.isfile('arquivo.txt'), 'Retorna um booleano')
print(os.path.isdir('diretorio_exemplo'), 'Retorna um booleano')

# Criar e remover diretórios
os.makedirs('novo_diretorio/subdiretorio', exist_ok=True)
os.makedirs('elisio/dasdrogas/cocaaaa', exist_ok=True)
#os.rmdir('novo_diretorio/subdiretorio')
#os.rmdir('novo_diretorio')
