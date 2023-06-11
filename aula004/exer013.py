print("\nCálculo do gasto por quilowatts consumidas\n")
salario = float(input("Insira o salário mínimo: "))
kw = float(input("Insira o quilowatt consumido: "))

valor_kw = salario/8
valor_pagar = valor_kw * kw
valor_desconto = valor_pagar - (valor_pagar/100 * 15)

print(f"O valor a pagar de cada quilowatt é de {valor_kw:.2f} R$")
print(f"O valor a ser pago pela residência é de {valor_pagar:.2f} R$")
print(f"O valor a ser pago com um desconto de 15% é de {valor_desconto:.2f} R$")
