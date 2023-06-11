dep = float(input("Insira um valor para depósito: "))
taxa = float(input("Insira o valor da taxa de juros (em %): "))

rend = dep * taxa/100 * 1

mont = rend + dep

print(f"O valor do rendimento mensal é de R$ {rend:.2f}")
print(f"O valor do montante é de R$ {mont:.2f}")