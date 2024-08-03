import random

palavras = ['python', 'desenvolvimento', 'programação', 'tecnologia', 'algoritmos']

palavra_secreta = random.choice(palavras)
letras_adivinhadas = []
tentativas = 6

print('Bem vindo ao jogo da Forca!')
print(f'A palavra secreta tem {len(palavra_secreta)} letras.')
print("_" * len(palavra_secreta))

while tentativas > 0:
    letra = input("\nAdivinhe uma letra: ".lower())

    if len(letra) != 1:
        print("Por favor apenas uma letra.")
        continue

    if letra in letras_adivinhadas:
        print("Você já adivinhou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_secreta:
        print("Boa! A letra está na palavra.")
    else: tentativas -= 1
    print(f'Errou! Você tem {tentativas} tentativas restantes;')

    #Mostrar progresso do player
    palavra_mostrada = [letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta]
    print("".join(palavra_mostrada))

    if "_" not in palavra_mostrada:
        print("\nParabéns! Você adivinhou a palavra")
        break
else: print(f"\nVocê perdeu! A palavra secreta era '{palavra_secreta}'.")

print('Obrigado por jogar!')