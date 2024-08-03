import os
from pathlib import Path

# Criar um novo diretório na área de trabalho
diretorio_novo = Path.home() / 'Desktop' / 'NovoDiretorio'
diretorio_novo.mkdir(parents=True, exist_ok=True)

print(f'Diretório criado: {diretorio_novo}')

# Remover o diretório
diretorio_novo.rmdir()
print(f'Diretório removido: {diretorio_novo}')

