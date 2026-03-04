cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente.', end='')
print(f'O número {num} por extenso é: {cont[num]}')
      
