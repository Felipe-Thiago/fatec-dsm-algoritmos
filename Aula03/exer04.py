salario = float(input("Entre com seu salário: "))
aumento = float(input("Insira um percentual de aumento: "))

n_salario = salario * (1 + (aumento/100))


print(f"Salário Original.....: R${salario:8.2f}")
print(f"Percentual de Aumento: {aumento:11.2f}%")
print(f"Novo Salário.........: R${n_salario:8.2f}") #:8.2f delimita a quantidade de casas depois e antes da virgula