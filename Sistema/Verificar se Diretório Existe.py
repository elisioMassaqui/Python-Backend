import os
from pathlib import Path

# Verificar se o diretório Documentos existe
documentos = Path.home() / 'Documents' / 'wandistudio' / 'wandicode'
if documentos.exists():
    print(f'O diretório {documentos} existe.')
else:
    print(f'O diretório {documentos} não existe.')
