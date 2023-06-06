print("Comparativo de consumo de combustível")
veiculos = []
consumo = []
preco = 5.65

for i in range(1, 6):
    veiculos.append(input(f"Veiculo {i}: "))
    consumo.append(float(input("Km por litro: ")))

print("Relatório final")
menor_consumo = 0
for i in range(0, 5):
    custo = 1000 / consumo[i]
    gasto = custo * preco
    print(f"{i+1} - {veiculos[i]:10} - {consumo[i]:6.2f} - {custo:6.1f} litros - R$ {gasto:6.2f}")
    if (consumo[i] > consumo[menor_consumo]):
        menor_consumo = i
print(f"O menor consumo é do {veiculos[menor_consumo]}")