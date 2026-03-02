soma = cont = 0
while True:
    num = int(input('999 para parar o programa: '))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'A soma dos valores foi {soma}')


