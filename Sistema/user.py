import os
from pathlib import Path

directorio_usuario_os = os.path.expanduser('~')
print("Usuário com os:", directorio_usuario_os, '\n')

directorio_usuario_path = Path.home()
print("Usuário com path:", directorio_usuario_path, '\n')
