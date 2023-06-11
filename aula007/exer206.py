f = 0
while True:
    n = int(input("Digite um número natural para seu fatorial: "))
    if n >= 0:
        break

if n == 0 or n == 1:
    f = 1
else:
    f = 1
    for i in range(1, n+1):
        f = f * i
        #ou f *= i

print(f"O fatorial de {n} é igual a {f}")
