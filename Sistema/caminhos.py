import os
from pathlib import Path

#Obter o directório do caminho documentos do usuário
documentos = Path.home() / 'Documents'
print('Caminho documentos:', documentos)