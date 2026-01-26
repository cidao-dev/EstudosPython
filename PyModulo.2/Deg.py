casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario: "))
anos = int(input("Quantos anos voce vai pagar: "))

qtd_meses = anos * 12
mensal = casa / qtd_meses

limite = salario * (30/100)

print(f"Para  pagar uma casa de {casa:.2f} em {anos} anos")
print(f"a prestacao sera de RS{mensal:.2f}")

if (mensal > limite):
    print('Emprestimo Negado')
else:
    print("Emprestimo Aprovado")