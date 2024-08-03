# With já cria um gerenciador de contexto "arquivo"
# Porque qunando ele sai do escopo ou seja fora da tabulação
# Do documento o arquivo é fechado
# Pra prevenir vulnerabilidade no software.

with open('arquivo.txt', 'r') as arquivo:
    ler = arquivo.read()
    print(ler)