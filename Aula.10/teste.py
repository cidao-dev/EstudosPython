n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A média da sua nota foi {m:.1f}')
print('Parabéns' if m>= 6 else 'Estude mais')