import os
import subprocess
import random

# Define o diretório base
base_directory = os.path.join(os.path.expanduser('~'), 'Documents', 'wandistudio', 'wandicode')

# Solicita ao usuário o nome do esboço
sketch_name = input("Digite o nome do esboço (deixe em branco para nome automático): ").strip()

# Se o usuário não fornecer um nome, cria um nome automático
if not sketch_name:
    random_number = random.randint(10, 99)
    sketch_name = f"wandicode{random_number}"

# Constrói o caminho completo para o esboço
sketch_path = os.path.join(base_directory, sketch_name)

# Cria o diretório, se necessário
os.makedirs(base_directory, exist_ok=True)

# Comando para criar o esboço usando Arduino CLI
create_sketch_command = f'arduino-cli sketch new "{sketch_path}"'
subprocess.run(create_sketch_command, shell=True)


print(f"Esboço criado em: {sketch_path}")
