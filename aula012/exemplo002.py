def soma(n, m):
    resultado = n + m
    return resultado

print("Soma...")
print(f"2 + 5 = {soma(2,5)}")

#ou

def soma2(n1, n2):
    return n1 + n2

print("-------------------------\nSoma 2...")
a = int(input("Digite o valor 1: "))
b = int(input("Digite o valor 2: "))
print(f"O valor da soma de {a} e {b} é igual a {soma2(a, b)}")

#ou


print("-------------------------\nSoma 3...")
resultado = 0
x = int(input("Digite o valor 1: "))
y = int(input("Digite o valor 2: "))
print(f"O valor da soma de {x} e {y} é igual a {soma(x, y)}")
print(f"A variável resultado vale neste momento: {resultado}")
