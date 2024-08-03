carta = input('Digite oba se tiver carta de motorista ou not se não tens: ')
idade = int(input('Digite a sua idade: '))

if carta == 'oba' and idade == 19: print(f"Tudo bem pode passar com seu '{carta}', com sua idade '{idade}'")
else: print('Dados inválidos')