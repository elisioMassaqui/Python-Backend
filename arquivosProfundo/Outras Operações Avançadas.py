import shutil

# Criar e escrever em um novo arquivo de texto
with open('relatorio.txt', 'w', encoding='UTF-8') as file:
    file.write('Este é o conteúdo do relatório.\n')
    file.write('Adicione mais informações aqui.')

# Copiar um arquivo com tudo lá dentro
    shutil.copy('arquivo.txt', 'copiado_arquivo.txt')
# Mover um arquivo
shutil.move('hei.txt', 'novo_diretorio/hei.txt')



