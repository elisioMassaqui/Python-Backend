#fantastico, python compara até string

idade = int(input('Digite sua idade: '))
carta = input("Digite caso possua ou não, uma carta de motorista, com 'sim' ou 'não': ")

if idade >= 18 and carta == 'sim':
    print("Você já pode dirigir")
elif idade <= 18 and carta == 'sim':
    print('Você não poderia ter carta, veja sua situação')
elif idade < 18 and carta == 'não':
    print('Espere seus 18 anos pra tirar carta')
elif idade >= 18 and carta == 'não':
    print('Você já pode tirar a sua carta')
else:
    print('hummmmmh')