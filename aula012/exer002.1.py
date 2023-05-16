n = int(input("Digite um número primo: "))

def eprimo(n):
    contador = 0

    for i in range(1, n+1):
        if (n % i) == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

if eprimo(n):
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")

print(f"({eprimo(n)})")

