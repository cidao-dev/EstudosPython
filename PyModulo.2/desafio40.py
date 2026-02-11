nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'''A sua PRIMEIRA nota foi {nota1} e sua SEGUNDA nota foi 
{nota2}. A média das nota é {media:.2f}''')

if 7 > media >= 5:
    print('REPROVADO')

elif media < 5:
    print('RECUPERAÇÃO')

elif media >= 7:
    print('APROVADO')