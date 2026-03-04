times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Atlético', 'Vasco', 'Chapecoense', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Liste os times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}')

