from random import randint
computador = randint (0,10)
print('Sou o seu computador ... Acabei de pensar em um número.')
print('Consegue advinhar qual número foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: 
            print(' Tá quaaaase ... tente outra vez para mais ...')
        elif jogador > computador: 
            print('Tá quaaaaase ... tente mais uma vez para menos ...')
print(f'Acertou com {palpites} tentativas. Parabéns!')