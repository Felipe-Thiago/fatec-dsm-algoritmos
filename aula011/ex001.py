lista = []
for i in range(1, 11):
    a = (int(input(f"Digite o {i}º número: ")))
    lista.append(a)

lista.reverse()
tupla = tuple(lista)

print(tupla)
print(type(tupla))


tupla2 = ()

for i in range(1, 11):
    b = int(input(f"Digite o {i}º número: "))
    tupla2 = tupla2 + (b,)


print(tupla2[::-1])
print(type(tupla2))