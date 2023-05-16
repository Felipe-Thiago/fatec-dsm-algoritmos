n = int(input("Digite um número par: "))

def epar(n):
    return n%2 == 0

if epar(n):
    print(f"Isso mesmo, o número {n} é par")
else:
    print(f"Errado, o número {n} é impar")
print(f"({epar(n)})")
