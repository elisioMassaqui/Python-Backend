nome = input("Por favor, Digite o seu nome: ")
anosNascimento = input('Por favor, Digite em que ano você nasceu: ')

#Não deveria ser assim, problema de operação e conversão não resovlido.
x = 2024 - 2002
print('Olá {}, de {} anos de idade {}, como vai a vida? '.format(nome, anosNascimento, x))