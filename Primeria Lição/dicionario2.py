#Chave é o nome de uma posição ou indice,prefixo
#E o sufixo é o valor
#Elisio = {'Nome': input('Digite seu nome:\n'),
#           'Idade': int(input('Digite a idade:\n')),
#           'Cidade': input('Digite sua cidade:\n'),
#           'País': input('Digite seu país:\n')
#        }

#Otimo pra definir nomes de local onde vai
#Um valor especifico sobre alguém dentro de uma
#Struct de python

#print(Elisio)

pessoas = {'Nomes': [],
           'Idades': [],
        }

while True:

    inciar = 1
    decisao = int(input('Digite 1 pra cadastrar uma pessoa ou qualquer numero pra sair do programa: '))

    if not True  == decisao == inciar:
        break

    pessoas['Nomes'].append(input('Digite seu nome:\n')),
    pessoas['Idades'].append(int(input('Digite a idade:\n')))

    print(pessoas)

tamanho = len(pessoas['Nomes'])

for i in range(0, tamanho):
    print(f'Nome: {pessoas["Nomes"][i]}')
    print(f'Idade {pessoas["Idades"][i]}')