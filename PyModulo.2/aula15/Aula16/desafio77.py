palavras = ('aprender', 'estudar', 'programar', 'python', 'javas'
            'gtinfo', 'vencer', 'malhar', 'esposa', 'filho', 'trabalhar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra, end='')
