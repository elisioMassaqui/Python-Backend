import tempfile
from pathlib import Path

diretorio_temporario = Path(tempfile.gettempdir())
print(f'Diretório Temporário: {diretorio_temporario}')