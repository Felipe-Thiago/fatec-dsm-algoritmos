import math
e = 0
n = int(input("Digite um número-limite de expoentes para a soma: "))
b = int(input("Digite o valor da base: "))
i = 1
while i <= n:
    e = e + math.pow(b, i)
    i += 1

print(f"O valor do expoente e é de: {e:.2f}")