def fatorial(n):
    if n > 1:
        return n * fatorial(n-1)
    else:
        return 1

n = int(input("Insira um número: "))
print(f"O fatorial de {n} é {fatorial(n)}")