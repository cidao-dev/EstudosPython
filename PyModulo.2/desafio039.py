from datetime import date

atual = date.today().year
data = int(input('Digite a sua data de nascimento: '))
genero = int(input('Você é homem ou mulher? '))
idade = atual - data

print(f'Quem nasceu {data} tem {idade} anos.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE. ')

elif idade < 18:
   saldo = 18 - idade
   print(f'Ainda faltam {saldo} para o seu alistamento militar. ')
   ano = atual + data
   print(f'Seu alistamento será em {data}.')

elif idade > 18:
    saldo = 18 - idade
    print(f'Você já deveria ter se alistado há {idade} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {data}')

else:
    print(f'Mulher não pode se alistar {genero}')
    


