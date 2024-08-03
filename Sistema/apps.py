import os
from pathlib import Path

if os.name == 'nt':
    dir_apps = Path('C:/Program Files')
else:
    dir_apps = Path('/usr/local/bin')

print(f'Dir de app: {dir_apps}')