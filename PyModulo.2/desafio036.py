print('EMPRESTIMO BANCÁRIO')

casa = float(input('Qual o valor da casa: R$ '))
salário = float(input('Qual o salário do comprador: R$ '))
anos = int(input('Financiamento de quantos anos: '))

prestação = casa / (anos*12)
mínimo = salário * (30/100)

print(f'NEGADO' if prestação > mínimo else 'APROVADO')
print(f'Sua prestação ficou no valor de {prestação:.2f} ')
print('O Banco Master agradeço a sua escolha.')