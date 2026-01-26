vel = int(input('Qual a velocidade que o carro estava? '))
if vel > 80:
    mul = (vel - 80)*7
    print('O valor da multa é de R$ 7,00 por cada km/h excedido. ')
    print(f'Você foi multado! Você pagará uma multa de {mul:.2f}')
print('Pague o quanto antes.')    