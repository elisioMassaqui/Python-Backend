import subprocess
from pathlib import Path

nomeApp = input('Introduza nome do app com ou sem a sua extensão que deve estar na pasta documentos:')

app_path = Path.home() / 'Documents' / nomeApp
subprocess.Popen([str(app_path)])