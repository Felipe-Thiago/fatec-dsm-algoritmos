idades = {
    "ana": 34,
    "pedro": 31,
    "josé": 45,
    "joão": 18
}

soma = 0
for idade in idades.values():
    print("A idade que está sendo somada agora é", idade)
    soma += idade

media = soma / len(idades)

print(f"A soma das idades é {soma}")
print(f"A média das idades é {media}")

print("\n============================\n")

maior = 0
maior_nome = ""
for nome in idades.keys():
    if len(nome) > maior:
        maior = len(nome)
        maior_nome = nome
print(f"O maior nome é o de {maior_nome} com {maior} letras e {idades.get(maior_nome)} anos")
