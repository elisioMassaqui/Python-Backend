#Use o módulo os.path ou o módulo pathlib 
# para manipular caminhos de arquivos.

from pathlib import Path

# Caminho absoluto, de algo que ainda nºao existe 
# Poraas paito é pai grande
p = Path('elisio.cs').resolve()
print(f"Caminho absoluto: \n {p}")

# Verificar se o arquivo existe
print(f"Veridicar se o arquivo existe: {p.exists()}")

# Criar um novo arquivo
p.touch()

## Remover um arquivo
p.unlink()

