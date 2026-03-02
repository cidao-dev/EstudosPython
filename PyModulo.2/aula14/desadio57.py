
sexo = str(input('Informe o seu sexo: [M/F] ')).strip() .upper()[0]
while sexo not in 'MmFf':
    sexo = str(int(input('Dados inválidos. Informe o sexo: '))).strip().upper()[0]
print(f'Sexo {sexo} registrado corretamente.')


