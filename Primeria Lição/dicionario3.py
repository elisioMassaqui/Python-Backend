pessoas = []



while True:
    inciar = 1
    decisao = int(input('Digite 1 pra cadastrar uma pessoa ou qualquer numero pra sair do programa: '))

    if not True  == decisao == inciar:
        break

    #Cada diciionario representa uma entidade
    nome = input('Digite seu nome:\n')
    idade = int(input('Digite a sua idade:\n'))

    pessoas.append({'nome': nome, 'idade': idade})

for i in pessoas:
    print(f'Nome: {i["nome"]}')
    print(f'Idade: {i['idade']}')
    print('*'*10)