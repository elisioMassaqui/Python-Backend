import subprocess
from pathlib import Path

# Caminho para o arquivo MSI
arduinoCLI = Path.home() / 'Documents' / 'wandistudio' / 'CLI' / 'arduino-cli_1.0.2_Windows_64bit.msi'

# Executar o instalador MSI usando msiexec
subprocess.Popen(['msiexec', '/i', str(arduinoCLI)], shell=True)
