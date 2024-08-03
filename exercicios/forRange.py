score = float(input('A sua pontuação: '))
maxScore = 50

for i in range(0, maxScore):
    if i == score < maxScore:
        break

print('Você excedeu o limite com: {}'.format(score))
print('Limite de scores: {}'.format(maxScore))
print('Verificação percorrida até: {}'.format(i))
