nome = str(input('Qual é o sei nome? '))
if nome ==  'Rodrigo':
    print('Seu nome é lindo.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paula':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Nome bem feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um ótimo dia!')