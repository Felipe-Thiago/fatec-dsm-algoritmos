def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f"Ocorreu um problema: {erro}"

n1 = int(input("Informe o dividendo: "))
n2 = int(input("Informe o divisor: "))
print(divisao(n1/n2))