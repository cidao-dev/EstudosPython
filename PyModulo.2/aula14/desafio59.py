from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('''          [1] SOMA
          [2] MULTIPLICAR
          [3] MAIOR
          [4] NOVOS NÚMEROS
          [5] SAIR DO PROGRAMA''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A Soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4: 
        print('Informe outro valor.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção ==5:
        print('Finalizando ...')
    else:
        print('Oplão inválida. Tente novamente.')
    print('==-==' * 10)
    sleep(2)
print('Fim do programa. Volte sempre.')
