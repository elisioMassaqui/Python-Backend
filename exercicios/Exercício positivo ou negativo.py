#Como sei se um numero é negativo ou positivo ou neuttro

valor = float(input('Digite um valor: '))

#Porque todo numero maior que zero é positivo
#E todo numero menor que 0 é negativo
#Todo numero que não é maior ou menor que 0 
#É neutro

if valor > 0: print('Positivo')
elif valor < 0: print('Negativo')
else: print('Neutro')