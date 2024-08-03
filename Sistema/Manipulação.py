import os 
from pathlib import Path

documentos = Path.home() / 'Documents' / 'wandistudio' / 'wandicode'
for arquivo in documentos.iterdir():
    print('Diretorios iterados kkkk: \n', arquivo)