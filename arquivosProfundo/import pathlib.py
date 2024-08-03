from pathlib import Path

# Caminho absoluto
p = Path('elisio.txt').resolve()
print('Caminho absoluto:\n', p, '\n')

print("É absoluto: ", p.is_absolute())

print("O absoluto existe?:", p.exists())
print("É ficheiro:", p.is_file())
print("É diretorio:", p.is_dir())

# Criar e remover diretórios
novo_dir = Path('novo_dir')
novo_dir.mkdir(parents=True, exist_ok=True)
print("Novo directorio:", novo_dir)
(subdir := novo_dir / 'subdir').mkdir()
print('Novo subdiretorio:', subdir)