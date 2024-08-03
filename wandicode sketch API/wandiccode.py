import os 
import subprocess
import random
from pathlib import Path

prefixo = 'wandicoe'
sufixo = random.randint(10, 200)

#Diretorio base
wandicode = os.path.join(os.path.expanduser('~'), 'Documents', 'wandistudio', 'wandicode')

#O strip é usado pra usuarios loucos que podem deixar whitespaces
code_name = input('Digite o nome de um esboço (deixe em branco para nome automático): ').strip()

#Se o usuário não fornecer um nome cria um nome automático
if not code_name:
    code_name = f'{prefixo}{sufixo}'
    print(code_name)

#Constrói o caminho completo para o esboço
code_path = os.path.join(wandicode, code_name)

#Cria o diretorio, se necessário
os.makedirs(wandicode, exist_ok=True)

#Comando pra criar o esboço 
criar_code = f'arduino-cli sketch new "{code_path}"'
#Chama o processo
subprocess.run(criar_code, shell=True, capture_output=True)

print(f'Esboço criado com sucesso em: {code_path}')