numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

numero = int(input('Digite um número entre 0 e 20: '))

if 0 <= numero <= 20:
    print(f'O número {numero} por extenso é: {numeros[numero]}')
else:
    print('Número fora do intervalo! Digite entre 0 e 20.')
