import os

arquivo = open('codigo.ino', 'w', encoding='UTF-8')

def load_code():
    # Determina o caminho da pasta Documentos do usuário
    documents_folder = os.path.join(os.environ['USERPROFILE'], 'Documents') if os.name == 'nt' else os.path.join(os.environ['HOME'], 'Documents')

    # Define o caminho da pasta wandi-studio, wandicode e do arquivo para carregar o código
    studio_folder = os.path.join(documents_folder, 'wandi-studio', 'wandicode')
    file_path = os.path.join(studio_folder, 'wandicode.ino')
    
    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        return print({"message": "Arquivo wandicode.ino não encontrado."}), 404

    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            code = file.read()
            arquivo.write(code)
        return print({"code": code})
    except Exception as e:
        return print({"message": f"Erro ao ler o código: {str(e)}"}), 500

load_code()