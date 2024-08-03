from pathlib import Path
import os

os.makedirs('downloads', exist_ok=True)

with open('arquivo_exemplo.txt', 'w') as file:
    print(file)

# Obter o caminho absoluto e verificar se é um arquivo ou diretório
p = Path('downloads/arquivo_exemplo.txt')

# Caminho absoluto
print(f'Caminho absoluto: {p.resolve()}')

# Verificar se é um arquivo ou diretório
print(f'É um arquivo? {p.is_file()}')
print(f'É um diretório? {p.is_dir()}')
