num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converter 
      [1] Converta para Binário
      [2] Converta para Octal
      [3] Converta para Hexadecimal ''')

opção = int(input('Sua opção foi: '))

if opção == 1:
    print(f'{num} convertido para Binário é: {bin(num)[2:]}')

elif opção == 2:
    print(f'{num} convertido para Octal é: {oct(num)[2:]}')

elif opção == 3:
    print(f'{num} convertido para Hexadecimal é: {hex(num)[2:]}')

else:
    print('OPÇÃO INVÁLIDA. TENTE OUTRA VEZ')