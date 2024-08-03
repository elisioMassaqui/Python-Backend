#Definição de funções e seus parametros

#Comparando vos valores de parametro pra casamento dá certo
def printar(x = 10, y = 20, z = 8):

    if x > 5 and y < 30 and z > 5:
        print('Olá, Mundo')
printar()

#Primeiro definir parametros depois colocar valor
#E depois somar, deixar tudo feito pra ser usado
#Noutra função
def soma(n1, n2):
    print(f'A soma entre {n1} e {n2} é = {n1+n2} ')
soma(n1= 2, n2= 5)


#Pegar tudo feito da função soma 
#Pra somar com paramentros dessa função
#Paramatros vs parametros
def pegarSoma(x=2, y=3):
    somar =  soma(n1=3 + x, n2= 2 + y) 

pegarSoma()

#Pegar tudo que já está aprimorado três vezes atrás
def pegarSomaDaSoma():
    pegarSoma()
pegarSomaDaSoma()