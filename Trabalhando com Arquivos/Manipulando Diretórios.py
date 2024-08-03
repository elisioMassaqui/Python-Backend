#Listar Arquivos e Diretórios
#Você pode listar arquivos 
#E diretórios usando o módulo os.
import os
# Listar arquivos e diretórios no diretório atua
itens = os.listdir('.')
print(itens)

#Criar e Remover Diretórios
os.makedirs('novo_diretorio', exist_ok=True)
os.makedirs('novo', exist_ok=True)
#os.mkdir('make')

# Remover um diretório
os.rmdir('novo_diretorio')
#Renomear e Mover Arquivos
os.rename('hello.text', 'wandi.text')

# Mover um arquivo para um novo diretório
os.rename('wandi.text', 'novo/wandi.text')
