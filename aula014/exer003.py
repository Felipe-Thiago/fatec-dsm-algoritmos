lista = []
soma = 0
multi = 1

num = str(input("Insira um número: "))

for i in num:
    lista.append(i)

for j in lista:
    soma = soma + int(j)
    multi = multi * int(j)

print(f"Número: {num}")
print(f"Multiplicação: {multi}")
print(f"Soma: {soma}")
